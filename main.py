import pygame

def JudgeAccuracy(points, c, max_error):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    total_err = 0
    valid = True
    prct_correct = 0
    dists = []

    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        dist = ((x - c[0]) ** 2 + (y - c[1]) ** 2) ** 0.5
        dists.append(dist)
    r = sum(dists) / len(dists)  # Average distance from center to points

    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        diff = dists[i]- r
        if abs(diff) > max_error:
            valid = False
        else:
            total_err += abs(diff)
    if valid:
        prct_correct = 100 * (1 - (total_err / (len(xs) * max_error)))
    return valid, prct_correct 

def main():
    pygame.init()
    x_size, y_size = 800, 800
    screen = pygame.display.set_mode((x_size, y_size))
    pygame.display.set_caption("Circle Drawing Accuracy Judge")

    center = (x_size / 2, y_size / 2)
    drawing = False
    points = []

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                points = []
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing:
                points.append(event.pos)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    points = []

        screen.fill((255, 255, 255))
        # Draw center cross
        pygame.draw.line(screen, (0, 0, 0), (center[0] - 10, center[1]), (center[0] + 10, center[1]), 2)
        pygame.draw.line(screen, (0, 0, 0), (center[0], center[1] - 10), (center[0], center[1] + 10), 2)
        # Draw user line
        if len(points) > 1:
            pygame.draw.lines(screen, (255, 0, 0), False, points, 2)

        max_distance = 50

        if len(points) > 0:
            valid, prct_correct = JudgeAccuracy(points, center, max_distance)
            if valid:
                result_text = f"Valid Circle! Accuracy: {prct_correct:.2f}%"
            else:
                result_text = "Invalid Circle!"
            font = pygame.font.Font(None, 36)
            text_surface = font.render(result_text, True, (0, 0, 0))
            screen.blit(text_surface, (20, 20))

        pygame.display.flip()
    pygame.quit()
    
main()