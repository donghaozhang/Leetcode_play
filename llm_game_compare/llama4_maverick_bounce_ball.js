// Number of balls
const NUM_BALLS = 10;

// Array to store balls
let balls = [];

// Rotation angle
let angle = 0;

function setup() {
  createCanvas(600, 600);
  angleMode(DEGREES);

  // Initialize balls
  for (let i = 0; i < NUM_BALLS; i++) {
    balls.push(new Ball(random(width), random(height)));
  }
}

function draw() {
  background(220);

  // Center of the hexagon
  let centerX = width / 2;
  let centerY = height / 2;

  // Draw rotating hexagon
  push();
  translate(centerX, centerY);
  rotate(angle);
  noStroke();
  fill(255, 204, 0, 50);
  beginShape();
  for (let i = 0; i < 6; i++) {
    let a = i * 60;
    let x = cos(a) * 200;
    let y = sin(a) * 200;
    vertex(x, y);
  }
  endShape(CLOSE);
  pop();

  // Update and display balls
  for (let i = 0; i < balls.length; i++) {
    balls[i].update();
    balls[i].display();
    balls[i].collide(balls.slice(i + 1));
    balls[i].checkHexagonCollision(centerX, centerY, angle);
  }

  // Increase rotation angle
  angle += 1;
}

// Ball class
class Ball {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.vx = random(-5, 5);
    this.vy = random(-5, 5);
    this.r = random(10, 30);
    this.c = color(random(255), random(255), random(255));
    this.elasticity = 0.8;
    this.friction = 0.98;
  }

  update() {
    this.vy += 0.1; // gravity
    this.x += this.vx;
    this.y += this.vy;

    // Apply friction
    this.vx *= this.friction;
    this.vy *= this.friction;
  }

  display() {
    fill(this.c);
    noStroke();
    ellipse(this.x, this.y, this.r * 2);
  }

  collide(others) {
    for (let other of others) {
      let dx = this.x - other.x;
      let dy = this.y - other.y;
      let distance = sqrt(dx * dx + dy * dy);
      let minDistance = this.r + other.r;

      if (distance < minDistance) {
        // Collision detected
        let normalX = dx / distance;
        let normalY = dy / distance;
        let tangentX = -normalY;
        let tangentY = normalX;

        let v1n = this.vx * normalX + this.vy * normalY;
        let v1t = this.vx * tangentX + this.vy * tangentY;
        let v2n = other.vx * normalX + other.vy * normalY;
        let v2t = other.vx * tangentX + other.vy * tangentY;

        let v1nAfter = (v1n * (this.elasticity - 1) + 2 * other.elasticity * v2n) / (this.elasticity + other.elasticity);
        let v2nAfter = (v2n * (other.elasticity - 1) + 2 * this.elasticity * v1n) / (this.elasticity + other.elasticity);

        this.vx = v1nAfter * normalX + v1t * tangentX;
        this.vy = v1nAfter * normalY + v1t * tangentY;
        other.vx = v2nAfter * normalX + v2t * tangentX;
        other.vy = v2nAfter * normalY + v2t * tangentY;
      }
    }
  }

  checkHexagonCollision(centerX, centerY, angle) {
    push();
    translate(centerX, centerY);
    rotate(angle);

    // Check collision with hexagon edges
    for (let i = 0; i < 6; i++) {
      let a1 = i * 60;
      let a2 = (i + 1) * 60;
      let x1 = cos(a1) * 200;
      let y1 = sin(a1) * 200;
      let x2 = cos(a2) * 200;
      let y2 = sin(a2) * 200;

      let distance = this.pointToLineDistance(this.x - centerX, this.y - centerY, x1, y1, x2, y2);

      if (distance < this.r) {
        // Collision detected
        let normalX = (y2 - y1);
        let normalY = -(x2 - x1);
        let length = sqrt(normalX * normalX + normalY * normalY);
        normalX /= length;
        normalY /= length;

        let tangentX = -normalY;
        let tangentY = normalX;

        let v1n = this.vx * normalX + this.vy * normalY;
        let v1t = this.vx * tangentX + this.vy * tangentY;

        v1n = -v1n * this.elasticity;

        this.vx = v1n * normalX + v1t * tangentX;
        this.vy = v1n * normalY + v1t * tangentY;
      }
    }

    pop();
  }

  pointToLineDistance(px, py, x1, y1, x2, y2) {
    let lineLengthSquared = (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1);
    if (lineLengthSquared == 0) return dist(px, py, x1, y1);

    let t = max(0, min(1, ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / lineLengthSquared));
    let nearestX = x1 + t * (x2 - x1);
    let nearestY = y1 + t * (y2 - y1);

    return dist(px, py, nearestX, nearestY);
  }
}