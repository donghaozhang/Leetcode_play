let dino, obstacles = [];
let groundHeight = 100;
let scrollSpeed = 5;
let score = 0;
let gameOver = false;
let highScore = 0;
let clouds = [];
let stars = [];
let isNight = false;
let dayLength = 10000; // 10 seconds
let currentTime = 0;

function setup() {
  createCanvas(800, 400);

  // Create dinosaur sprite
  dino = {
    x: 100,
    y: height - groundHeight - 30,
    width: 40,
    height: 60,
    gravity: 0.8,
    velocity: 0,
    jumpForce: -15,
    isJumping: false,
    // Animation frames (simple pixel art)
    frames: [
      [
        [0,15,0,0,0,15],
        [0,15,15,15,15,0],
        [15,15,15,15,15,15],
        [15,15,0,15,15,15],
        [0,15,15,15,15],
        [0,0,15,15,0,0]
      ],
      [
        [0,15,0,0,0,15],
        [0,15,15,15,15,0],
        [15,15,15,15,15,15],
        [15,15,0,15,15,15],
        [0,15,15,15],
        [0,0,15,15,15,15,0]
      ]
    ],
    frameCount: 0,
    currentFrame: 0,
    animateSpeed: 5
  };

  // Create initial clouds
  for (let i = 0; i < 10; i++) {
    clouds.push({
      x: random(width),
      y: random(height * 0.3),
      size: random(30, 70),
      speed: random(0.5, 1.5)
    });
  }

  // Create stars for night background
  for (let i = 0; i < 100; i++) {
    stars.push({
      x: random(width),
      y: random(height - groundHeight),
      size: random(1, 3),
      brightness: random(100, 255)
    });
  }

  // Instructions text
  textSize(16);
  textAlign(CENTER, CENTER);
}

function draw() {
  // Day/night cycle
  currentTime = (currentTime + deltaTime) % dayLength;
  isNight = currentTime > dayLength / 2;

  // Background
  if (isNight) {
    background(10, 20, 40);
    // Draw twinkling stars
    for (let star of stars) {
      fill(255, 255, 255, star.brightness);
      noStroke();
      ellipse(star.x, star.y, star.size);
      // Make some stars twinkle
      if (random() < 0.02) {
        star.brightness = random(100, 255);
      }
    }
    // Moon
    fill(220);
    ellipse(width - 100, 80, 60);
    fill(10, 20, 40);
    ellipse(width - 110, 70, 50);
  } else {
    // Day background gradient
    let gradientSky = drawingContext.createLinearGradient(0, 0, 0, height - groundHeight);
    gradientSky.addColorStop(0, color(135, 206, 235));
    gradientSky.addColorStop(1, color(176, 226, 255));
    drawingContext.fillStyle = gradientSky;
    noStroke();
    rect(0, 0, width, height - groundHeight);

    // Sun
    fill(255, 204, 0);
    ellipse(width - 100, 80, 60);
  }

  // Ground
  fill(isNight ? color(70, 70, 80) : color(144, 238, 144));
  noStroke();
  rect(0, height - groundHeight, width, groundHeight);

  // Clouds
  for (let cloud of clouds) {
    fill(255, 255, 255, isNight ? 100 : 255);
    ellipse(cloud.x, cloud.y, cloud.size);
    ellipse(cloud.x + cloud.size * 0.3, cloud.y - cloud.size * 0.1, cloud.size * 0.8);
    ellipse(cloud.x + cloud.size * 0.6, cloud.y, cloud.size * 0.7);
    cloud.x -= cloud.speed;
    if (cloud.x < -cloud.size) {
      cloud.x = width + cloud.size;
      cloud.y = random(height * 0.3);
    }
  }

  // Ground details (pixelated rocks and grass)
  drawGroundDetails();

  if (!gameOver) {
    // Update game elements
    updateDino();
    updateObstacles();
    spawnObstacles();
    score += 0.1;

    // Display score
    fill(0);
    textSize(24);
    textAlign(LEFT, TOP);
    text("Score: " + floor(score), 20, 20);
    text("High Score: " + floor(highScore), 20, 50);

    // Instructions
    textSize(16);
    textAlign(CENTER, CENTER);
    if (frameCount < 180) { // Display for first 3 seconds
      fill(0, 102, 153, 200);
      rect(width/2 - 150, height - 100, 300, 60);
      fill(255);
      text("Press SPACE to jump!", width/2, height - 70);
    }
  } else {
    // Game over screen
    fill(0, 0, 0, 150);
    rect(0, 0, width, height);

    fill(255);
    textSize(48);
    textAlign(CENTER, CENTER);
    text("GAME OVER", width/2, height/2 - 50);

    textSize(24);
    text("Score: " + floor(score), width/2, height/2 + 10);
    text("High Score: " + floor(highScore), width/2, height/2 + 50);

    textSize(20);
    text("Press R to restart", width/2, height/2 + 100);
  }
}

function drawGroundDetails() {
  // Draw pixelated ground details (rocks and grass)
  for (let i = 0; i < width; i += 20) {
    let yBase = height - groundHeight + 10;

    // Grass
    if (!isNight) {
      fill(34, 139, 34);
      for (let j = 0; j < 3; j++) {
        let bladeX = i + random(5, 15);
        let bladeHeight = random(5, 15);
        triangle(
          bladeX, yBase - bladeHeight,
          bladeX - 2, yBase,
          bladeX + 2, yBase
        );
      }
    }

    // Rocks
    if (random() < 0.03) {
      let rockSize = random(10, 25);
      fill(isNight ? color(100, 100, 120) : color(150, 150, 150));
      ellipse(i + rockSize/2, yBase - rockSize/4, rockSize, rockSize/2);
    }
  }
}

function updateDino() {
  // Apply gravity
  dino.velocity += dino.gravity;
  dino.y += dino.velocity;

  // Ground collision
  if (dino.y > height - groundHeight - dino.height) {
    dino.y = height - groundHeight - dino.height;
    dino.velocity = 0;
    dino.isJumping = false;
  }

  // Animate dinosaur
  dino.frameCount++;
  if (dino.frameCount % dino.animateSpeed === 0 && !dino.isJumping) {
    dino.currentFrame = (dino.currentFrame + 1) % dino.frames.length;
  }

  // Draw dinosaur
  let frame = dino.frames[dino.currentFrame];
  let pxSize = 5; // Size of each pixel in sprite
  let yOffset = 0;

  if (dino.isJumping) {
    // Use first frame when jumping
    frame = dino.frames[0];
  }

  for (let row = 0; row < frame.length; row++) {
    for (let col = 0; col < frame[row].length; col++) {
      if (frame[row][col]) {
        fill(frame[row][col] === 15 ? 0 : 255);
        if (frame[row][col] === 15) {
          rect(dino.x + col * pxSize, dino.y + row * pxSize - (frame.length * pxSize - dino.height), pxSize, pxSize);
        }
      }
    }
  }
}

function updateObstacles() {
  for (let i = obstacles.length - 1; i >= 0; i--) {
    obstacles[i].x -= scrollSpeed;

    // Draw obstacle (cactus)
    fill(isNight ? color(70, 90, 70) : color(34, 139, 34));
    rect(obstacles[i].x, obstacles[i].y, obstacles[i].width, obstacles[i].height);
    // Add some details to cactus
    fill(isNight ? color(60, 80, 60) : color(0, 100, 0));
    rect(obstacles[i].x + 5, obstacles[i].y + 5, 5, 10);

    // Collision detection
    if (
      dino.x + dino.width > obstacles[i].x &&
      dino.x < obstacles[i].x + obstacles[i].width &&
      dino.y + dino.height > obstacles[i].y
    ) {
      gameOver = true;
      if (score > highScore) {
        highScore = score;
      }
    }

    // Remove off-screen obstacles
    if (obstacles[i].x + obstacles[i].width < 0) {
      obstacles.splice(i, 1);
    }
  }
}

function spawnObstacles() {
  if (frameCount % floor(random(60, 120)) === 0) {
    let cactusHeight = random(40, 70);
    obstacles.push({
      x: width,
      y: height - groundHeight - cactusHeight,
      width: 30,
      height: cactusHeight
    });

    // Occasionally spawn a flying obstacle at night
    if (isNight && random() < 0.3) {
      obstacles.push({
        x: width,
        y: height - groundHeight - 150,
        width: 40,
        height: 30
      });
    }
  }
}

function keyPressed() {
  if ((key === ' ' || keyCode === UP_ARROW) && !dino.isJumping && !gameOver) {
    dino.velocity = dino.jumpForce;
    dino.isJumping = true;
    dino.currentFrame = 0; // Reset animation frame
  } else if (key === 'r' || key === 'R') {
    // Reset game
    if (gameOver) {
      obstacles = [];
      score = 0;
      gameOver = false;
      dino.y = height - groundHeight - 30;
      dino.velocity = 0;
      dino.isJumping = false;
      currentTime = 0;
    }
  }
}