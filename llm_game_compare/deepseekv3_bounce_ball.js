let balls = [];
let hexagonRotation = 0;
let hexagonSize = 250;
let gravity = 0.2;
let elasticity = 0.8;
let friction = 0.99;

function setup() {
  createCanvas(600, 600);

  // Create 10 colorful balls with random properties
  for (let i = 0; i < 10; i++) {
    balls.push({
      x: random(width * 0.25, width * 0.75),
      y: random(height * 0.25, height * 0.75),
      radius: random(15, 30),
      vx: random(-3, 3),
      vy: random(-3, 3),
      color: color(random(100, 255), random(100, 255), random(100, 255))
    });
  }
}

function draw() {
  background(30);

  // Update hexagon rotation
  hexagonRotation += 0.005;

  // Draw rotating hexagon
  push();
  translate(width/2, height/2);
  rotate(hexagonRotation);
  noFill();
  stroke(255, 150);
  strokeWeight(2);
  beginShape();
  for (let i = 0; i < 6; i++) {
    let angle = TWO_PI / 6 * i;
    let x = cos(angle) * hexagonSize;
    let y = sin(angle) * hexagonSize;
    vertex(x, y);
  }
  endShape(CLOSE);
  pop();

  // Update and draw all balls
  for (let ball of balls) {
    // Apply gravity
    ball.vy += gravity;

    // Apply friction
    ball.vx *= friction;
    ball.vy *= friction;

    // Update position
    ball.x += ball.vx;
    ball.y += ball.vy;

    // Check collision with hexagon walls
    checkHexagonCollision(ball);

    // Check collision with other balls
    for (let other of balls) {
      if (ball !== other) {
        checkBallCollision(ball, other);
      }
    }

    // Draw the ball
    fill(ball.color);
    noStroke();
    ellipse(ball.x, ball.y, ball.radius * 2);
  }
}

function checkHexagonCollision(ball) {
  // Convert ball position to hexagon's rotated coordinate system
  let centerX = width/2;
  let centerY = height/2;
  let dx = ball.x - centerX;
  let dy = ball.y - centerY;

  // Rotate the point back to align with unrotated hexagon
  let angle = -hexagonRotation;
  let rotatedX = dx * cos(angle) - dy * sin(angle);
  let rotatedY = dx * sin(angle) + dy * cos(angle);

  // Check collision with each hexagon edge
  let closestDist = Infinity;
  let closestNormal = createVector(0, 0);

  for (let i = 0; i < 6; i++) {
    let angle1 = TWO_PI / 6 * i;
    let angle2 = TWO_PI / 6 * ((i + 1) % 6);

    let x1 = cos(angle1) * hexagonSize;
    let y1 = sin(angle1) * hexagonSize;
    let x2 = cos(angle2) * hexagonSize;
    let y2 = sin(angle2) * hexagonSize;

    // Find closest point on edge
    let edge = createVector(x2 - x1, y2 - y1);
    let toPoint = createVector(rotatedX - x1, rotatedY - y1);
    let edgeLength = edge.mag();
    let edgeNorm = edge.copy().normalize();
    let projection = toPoint.dot(edgeNorm);

    projection = constrain(projection, 0, edgeLength);
    let closestPoint = createVector(x1, y1).add(edgeNorm.mult(projection));

    let distToEdge = createVector(rotatedX, rotatedY).dist(closestPoint);

    if (distToEdge < closestDist) {
      closestDist = distToEdge;
      closestNormal = createVector(rotatedX - closestPoint.x, rotatedY - closestPoint.y).normalize();
    }
  }

  // If ball is outside hexagon or touching edge
  if (closestDist < ball.radius) {
    // Calculate penetration depth
    let penetration = ball.radius - closestDist;

    // Move ball back inside hexagon
    let correction = closestNormal.copy().mult(penetration);
    rotatedX += correction.x;
    rotatedY += correction.y;

    // Rotate back to original coordinate system
    angle = hexagonRotation;
    let newX = rotatedX * cos(angle) - rotatedY * sin(angle) + centerX;
    let newY = rotatedX * sin(angle) + rotatedY * cos(angle) + centerY;

    // Calculate reflection of velocity
    let vel = createVector(ball.vx, ball.vy);
    let rotatedVelX = vel.x * cos(angle) - vel.y * sin(angle);
    let rotatedVelY = vel.x * sin(angle) + vel.y * cos(angle);
    let rotatedVel = createVector(rotatedVelX, rotatedVelY);

    let dot = rotatedVel.dot(closestNormal);
    rotatedVel.sub(closestNormal.mult(2 * dot));

    // Apply elasticity
    rotatedVel.mult(elasticity);

    // Rotate velocity back
    angle = -hexagonRotation;
    ball.vx = rotatedVel.x * cos(angle) - rotatedVel.y * sin(angle);
    ball.vy = rotatedVel.x * sin(angle) + rotatedVel.y * cos(angle);

    // Update position
    ball.x = newX;
    ball.y = newY;
  }
}

function checkBallCollision(b1, b2) {
  let dx = b2.x - b1.x;
  let dy = b2.y - b1.y;
  let distance = sqrt(dx * dx + dy * dy);

  if (distance < b1.radius + b2.radius) {
    // Calculate collision normal
    let nx = dx / distance;
    let ny = dy / distance;

    // Calculate relative velocity
    let vx = b2.vx - b1.vx;
    let vy = b2.vy - b1.vy;

    // Calculate relative velocity in terms of the normal direction
    let velAlongNormal = vx * nx + vy * ny;

    // Do not resolve if velocities are separating
    if (velAlongNormal > 0) return;

    // Calculate restitution (elasticity)
    let e = min(b1.radius, b2.radius) / max(b1.radius, b2.radius) * elasticity;

    // Calculate impulse scalar
    let j = -(1 + e) * velAlongNormal;
    j /= 1/b1.radius + 1/b2.radius;

    // Apply impulse
    let impulseX = j * nx;
    let impulseY = j * ny;

    b1.vx -= impulseX / b1.radius;
    b1.vy -= impulseY / b1.radius;
    b2.vx += impulseX / b2.radius;
    b2.vy += impulseY / b2.radius;

    // Move balls apart to prevent sticking
    let overlap = (b1.radius + b2.radius - distance) / 2.0;
    b1.x -= overlap * nx;
    b1.y -= overlap * ny;
    b2.x += overlap * nx;
    b2.y += overlap * ny;
  }
}