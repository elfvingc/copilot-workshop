const canvas = document.getElementById('pongCanvas');
const ctx = canvas.getContext('2d');

const SCREEN_WIDTH = 800;
const SCREEN_HEIGHT = 600;
const SCORE_PANE_HEIGHT = 50;

const WHITE = '#FFFFFF';
const BLACK = '#000000';

const PLAYER_WIDTH = 20;
const PLAYER_HEIGHT = 120;

let ball = {
    x: SCREEN_WIDTH / 2 - 15,
    y: SCORE_PANE_HEIGHT + 10,
    width: 30,
    height: 30,
    speedX: 7,
    speedY: 7
};

let player1 = {
    x: 50,
    y: SCREEN_HEIGHT / 2 + SCORE_PANE_HEIGHT - PLAYER_HEIGHT / 2,
    width: PLAYER_WIDTH,
    height: PLAYER_HEIGHT,
    speed: 0,
    score: 0
};

let player2 = {
    x: SCREEN_WIDTH - 70,
    y: SCREEN_HEIGHT / 2 + SCORE_PANE_HEIGHT - PLAYER_HEIGHT / 2,
    width: PLAYER_WIDTH,
    height: PLAYER_HEIGHT,
    score: 0
};

let keys = {
    ArrowUp: false,
    ArrowDown: false
};

function draw() {
    // Clear canvas
    ctx.fillStyle = BLACK;
    ctx.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT + SCORE_PANE_HEIGHT);

    // Draw score pane
    ctx.fillStyle = WHITE;
    ctx.fillRect(0, 0, SCREEN_WIDTH, SCORE_PANE_HEIGHT);

    // Draw players
    ctx.fillStyle = WHITE;
    ctx.fillRect(player1.x, player1.y, player1.width, player1.height);
    ctx.fillRect(player2.x, player2.y, player2.width, player2.height);

    // Draw ball
    ctx.beginPath();
    ctx.fillStyle = WHITE;
    ctx.arc(
        ball.x + ball.width / 2,  // Center x-coordinate
        ball.y + ball.height / 2, // Center y-coordinate
        ball.width / 2,           // Radius
        0,                        // Start angle
        Math.PI * 2               // End angle (full circle)
    );
    ctx.fill();
    ctx.closePath();

    // Draw scores
    ctx.fillStyle = BLACK;
    ctx.font = '36px Arial';
    ctx.fillText('Player 1: ' + player1.score, 50, 36);
    ctx.fillText('Player 2: ' + player2.score, SCREEN_WIDTH - 200, 36);
}

function update() {
    // Move player1
    if (keys.ArrowUp && player1.y > SCORE_PANE_HEIGHT) {
        player1.y -= 7;
    }
    if (keys.ArrowDown && (player1.y + player1.height < SCREEN_HEIGHT + SCORE_PANE_HEIGHT)) {
        player1.y += 7;
    }

    // Move player2
    if (ball.y < player2.y) {
        player2.y = ball.y;
    } else if (ball.y + ball.height > player2.y + player2.height) {
        player2.y = ball.y - player2.height;
    }
    if (player2.y < SCORE_PANE_HEIGHT) {
        player2.y = SCORE_PANE_HEIGHT;
    }

    let previousBallLeft = ball.x;
    let previousBallRight = ball.x + ball.width;
    let previousBallTop = ball.y;
    let previousBallBottom = ball.y + ball.height;
    let player1Left = player1.x;
    let player1Right = player1.x + player1.width;
    let player1Top = player1.y;
    let player1Bottom = player1.y + player1.height;
    let player2Left = player2.x;
    let player2Right = player2.x + player2.width;
    let player2Top = player2.y;
    let player2Bottom = player2.y + player2.height;

    // Move ball
    ball.x += ball.speedX;
    ball.y += ball.speedY;

    // Ball collision with top and bottom
    if (ball.y <= SCORE_PANE_HEIGHT || ball.y + ball.height >= SCREEN_HEIGHT + SCORE_PANE_HEIGHT) {
        ball.speedY *= -1;
    }

    // Ball collision with left and right
    if (ball.x <= 0) {
        player2.score += 1;
        resetBall();
    } else if (ball.x + ball.width >= SCREEN_WIDTH) {
        player1.score += 1;
        resetBall();
    }

    // Ball collision with players
    if (isColliding(ball, player1)) {
        if (previousBallRight <= player1Left) {
            ball.x = player1Left;
            ball.speedX *= -1;
        } else if (previousBallLeft >= player1Right) {
            ball.x = player1Right;
            ball.speedX *= -1;
        } else if (previousBallBottom <= player1Top) {
            ball.y = player1Top;
            ball.speedY *= -1;
        } else if (previousBallTop >= player1Bottom) {
            ball.y = player1Bottom;
            ball.speedY *= -1;
        }
    }
    if (isColliding(ball, player2)) {
        if (previousBallRight <= player2Left) {
            ball.x = player2Left - ball.width;
            ball.speedX *= -1;
        } else if (previousBallLeft >= player2Right) {
            ball.x = player2Right;
            ball.speedX *= -1;
        } else if (previousBallBottom <= player2Top) {
            ball.y = player2Top;
            ball.speedY *= -1;
        } else if (previousBallTop >= player2Bottom) {
            ball.y = player2Bottom;
            ball.speedY *= -1;
        }
    }
}

function isColliding(rect1, rect2) {
    return rect1.x < rect2.x + rect2.width &&
        rect1.x + rect1.width > rect2.x &&
        rect1.y < rect2.y + rect2.height &&
        rect1.y + rect1.height > rect2.y;
}

function resetBall() {
    ball.x = SCREEN_WIDTH / 2 - 15;
    ball.y = SCREEN_HEIGHT / 2 - 15;
    ball.speedX = -ball.speedX;
}

function gameLoop() {
    update();
    draw();
    requestAnimationFrame(gameLoop);
}

document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowUp') {
        keys.ArrowUp = true;
    }
    if (event.key === 'ArrowDown') {
        keys.ArrowDown = true;
    }
});

document.addEventListener('keyup', (event) => {
    if (event.key === 'ArrowUp') {
        keys.ArrowUp = false;
    }
    if (event.key === 'ArrowDown') {
        keys.ArrowDown = false;
    }
});

gameLoop();

