// Game variables
let dino;
let obstacles = [];
let score = 0;
let gameOver = false;
let bg = [];
let groundY;
let jump = false;
let gravity = 0.5;

function setup() {
  createCanvas(800, 400);
  frameRate(60);
  rectMode(CORNER);
  imageMode(CORNER);

  // Initialize dinosaur
  dino = {
    x: 100,
    y: height / 2,
    w: 40,
    h: 40,
    vy: 0,
    onGround: true
  };

  // Initialize background
  for (let i = 0; i < 5; i++) {
    bg.push({
      x: i * width,
      y: 0,
      w: width,
      h: height,
      speed: -2
    });
  }

  groundY = height - 50;
}

function draw() {
  background(135, 206, 235); // Light blue sky

  // Draw and update background
  for (let i = 0; i < bg.length; i++) {
    drawBackground(bg[i]);
    updateBackground(bg[i]);

    // Check if background has moved off the screen
    if (bg[i].x < -width) {
      bg[i].x = bg[bg.length - 1].x + width;
    }
  }

  // Draw ground
  fill(139, 69, 19); // Brown
  noStroke();
  rect(0, groundY, width, 50);

  // Draw and update dinosaur
  drawDino(dino);
  updateDino(dino);

  // Draw and update obstacles
  for (let i = obstacles.length - 1; i >= 0; i--) {
    drawObstacle(obstacles[i]);
    updateObstacle(obstacles[i]);

    // Check for collision with dinosaur
    if (checkCollision(dino, obstacles[i])) {
      gameOver = true;
    }

    // Check if obstacle has moved off the screen
    if (obstacles[i].x < -obstacles[i].w) {
      obstacles.splice(i, 1);
      score++;
    }
  }

  // Generate new obstacles
  if (random(1) < 0.05 && !gameOver) {
    obstacles.push({
      x: width,
      y: groundY - 30,
      w: 30,
      h: 30,
      speed: -5
    });
  }

  // Display score
  fill(0);
  textSize(24);
  text(`Score: ${score}`, 20, 30);

  // Display game over screen
  if (gameOver) {
    fill(255, 0, 0); // Red
    textSize(48);
    textAlign(CENTER, CENTER);
    text("Game Over!", width / 2, height / 2);
    textSize(24);
    text("Press SPACE to restart", width / 2, height / 2 + 50);
    noLoop();
  }

  // Display key instructions
  fill(0);
  textSize(18);
  text("Press SPACE to jump", 20, height - 20);
}

function drawDino(dino) {
  // Draw pixelated dinosaur
  fill(0, 255, 0); // Green
  noStroke();
  rect(dino.x, dino.y, dino.w, dino.h);

  // Add some pixel art details
  fill(0); // Black
  rect(dino.x + 10, dino.y + 10, 5, 5); // Eye
  rect(dino.x + 20, dino.y + 20, 10, 5); // Mouth
}

function updateDino(dino) {
  if (jump && dino.onGround) {
    dino.vy = -10;
    dino.onGround = false;
    jump = false;
  }

  dino.vy += gravity;
  dino.y += dino.vy;

  if (dino.y + dino.h > groundY) {
    dino.y = groundY - dino.h;
    dino.vy = 0;
    dino.onGround = true;
  }
}

function drawBackground(bg) {
  // Draw background layers
  fill(34, 139, 34); // Forest green
  noStroke();
  rect(bg.x, bg.y, bg.w, bg.h);
}

function updateBackground(bg) {
  bg.x += bg.speed;
}

function drawObstacle(obstacle) {
  // Draw obstacles (cacti)
  fill(0, 255, 0); // Green
  noStroke();
  rect(obstacle.x, obstacle.y, obstacle.w, obstacle.h);
}

function updateObstacle(obstacle) {
  obstacle.x += obstacle.speed;
}

function checkCollision(dino, obstacle) {
  if (dino.x + dino.w > obstacle.x &&
      dino.x < obstacle.x + obstacle.w &&
      dino.y + dino.h > obstacle.y &&
      dino.y < obstacle.y + obstacle.h) {
    return true;
  }
  return false;
}

function keyPressed() {
  if (key === ' ') {
    if (gameOver) {
      // Restart game
      score = 0;
      gameOver = false;
      obstacles = [];
      dino.x = 100;
      dino.y = height / 2;
      dino.vy = 0;
      dino.onGround = true;
      loop();
    } else {
      jump = true;
    }
  }
}