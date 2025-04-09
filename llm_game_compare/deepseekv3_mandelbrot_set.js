let xmin = -2.5;
let xmax = 1;
let ymin = -1.5;
let ymax = 1.5;
let maxIterations = 100;
let zoomFactor = 0.5;

function setup() {
  createCanvas(800, 800);
  pixelDensity(1);
  drawMandelbrot();
}

function drawMandelbrot() {
  loadPixels();

  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      // Map pixel coordinates to complex plane coordinates
      let a = map(x, 0, width, xmin, xmax);
      let b = map(y, 0, height, ymin, ymax);

      // Original complex number
      let ca = a;
      let cb = b;

      let n = 0;

      // Iterate the Mandelbrot equation
      while (n < maxIterations) {
        let aa = a * a - b * b;
        let bb = 2 * a * b;

        a = aa + ca;
        b = bb + cb;

        // If the point escapes to infinity
        if (a * a + b * b > 4) {
          break;
        }

        n++;
      }

      // Color based on number of iterations
      let bright = map(n, 0, maxIterations, 0, 1);
      bright = map(sqrt(bright), 0, 1, 0, 255);

      // If point didn't escape, color it black
      if (n === maxIterations) {
        bright = 0;
      }

      let pix = (x + y * width) * 4;
      pixels[pix + 0] = bright;
      pixels[pix + 1] = bright;
      pixels[pix + 2] = bright / 2 + 50; // Slight reddish tint
      pixels[pix + 3] = 255;
    }
  }

  updatePixels();

  // Show coordinates
  noStroke();
  fill(255);
  textAlign(RIGHT, TOP);
  text(`X: [${xmin.toFixed(3)}, ${xmax.toFixed(3)}]\nY: [${ymin.toFixed(3)}, ${ymax.toFixed(3)}]`, width - 10, 10);
}

function mousePressed() {
  // On mouse click, zoom in on that point
  let newWidth = (xmax - xmin) * zoomFactor;
  let newHeight = (ymax - ymin) * zoomFactor;

  // Map mouse position to complex coordinates
  let mx = map(mouseX, 0, width, xmin, xmax);
  let my = map(mouseY, 0, height, ymin, ymax);

  // Adjust bounds
  xmin = mx - newWidth / 2;
  xmax = mx + newWidth / 2;
  ymin = my - newHeight / 2;
  ymax = my + newHeight / 2;

  // Redraw
  drawMandelbrot();
}

function keyPressed() {
  // Different keys for different actions
  if (key === ' ') { // Space to zoom out
    let centerX = (xmin + xmax) / 2;
    let centerY = (ymin + ymax) / 2;
    let newWidth = (xmax - xmin) / zoomFactor;
    let newHeight = (ymax - ymin) / zoomFactor;

    xmin = centerX - newWidth / 2;
    xmax = centerX + newWidth / 2;
    ymin = centerY - newHeight / 2;
    ymax = centerY + newHeight / 2;

    drawMandelbrot();
  } else if (key === '+' || key === '=') { // Increase iterations
    maxIterations += 20;
    drawMandelbrot();
  } else if (key === '-' || key === '_') { // Decrease iterations
    maxIterations = max(maxIterations - 20, 20);
    drawMandelbrot();
  } else if (key === 'r' || key === 'R') { // Reset view
    xmin = -2.5;
    xmax = 1;
    ymin = -1.5;
    ymax = 1.5;
    maxIterations = 100;
    drawMandelbrot();
  } else if (keyCode === LEFT_ARROW) { // Pan left
    let delta = (xmax - xmin) * 0.1;
    xmin -= delta;
    xmax -= delta;
    drawMandelbrot();
  } else if (keyCode === RIGHT_ARROW) { // Pan right
    let delta = (xmax - xmin) * 0.1;
    xmin += delta;
    xmax += delta;
    drawMandelbrot();
  } else if (keyCode === UP_ARROW) { // Pan up
    let delta = (ymax - ymin) * 0.1;
    ymin -= delta;
    ymax -= delta;
    drawMandelbrot();
  } else if (keyCode === DOWN_ARROW) { // Pan down
    let delta = (ymax - ymin) * 0.1;
    ymin += delta;
    ymax += delta;
    drawMandelbrot();
  }
}