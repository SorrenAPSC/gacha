import random
import time
import pygame

def main_gacha():
    
    # main gacha pool as file name
    gacha_girls = ["hutao.jpeg","mona.jpeg",
            "lisa.jpeg", "barbara.jpeg", "shogun.jpeg"]
    # Empty list of pulls used for inventory
    gacha_pulls = []

    # Counting variables to keep track of copies
    hutao_count = 0
    mona_count = 0
    lisa_count = 0
    barbara_count = 0
    shogun_count = 0

    # Equals 1000, can be scaled with added girls
    item_probs = [450, 450, 70, 29, 1]
    
    # Needed for calculation
    total_probs = sum(item_probs)
    

    def single_pull():
        
        roll = random.randint(0, total_probs)

        probability_counter = 0
        for i, item in enumerate(gacha_girls):
            probability_counter += item_probs[i]
            if roll <= probability_counter:
                print("roll:", roll)
                # Adds this pull to the inventory
                gacha_pulls.append(item)
                return item

    pygame.init()
    screen = pygame.display.set_mode((300, 300))

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    
        ready_to_pull = True
        while ready_to_pull:
            key_press = input("Ready to pull? Press K to start, Q to quit,\
 and 'I' to check inventory\n")
        
            if key_press.lower() == "k":
            
                time.sleep(1)
                gacha_image = pygame.image.load(single_pull())

    # Clear the screen
                screen.fill((255, 255, 255))

    # Draw the image to the screen at position (100, 100)
                screen.blit(gacha_image, (0, 0))

    # Update the display
                pygame.display.flip()

    # wait a moment to display image, then quit automatically
            elif key_press.lower() == "q":
                ready_to_pull = False
            elif key_press.lower() == "i":
                for i, item in enumerate(gacha_pulls):
                    if item == "hutao.jpeg":
                        hutao_count += 1
                    elif item == "mona.jpeg":
                        mona_count += 1
                    elif item == "lisa.jpeg":
                        lisa_count += 1
                    elif item == "barbara.jpeg":
                        barbara_count += 1
                    elif item == "shogun.jpeg":
                        shogun_count += 1

                print("Inventory:\n")
                time.sleep(0.2)
                print("Hutao's -", hutao_count, "\n")
                time.sleep(0.2)
                print("Mona's -", mona_count, "\n")
                time.sleep(0.2)
                print("Lisa's -", lisa_count, "\n")
                time.sleep(0.2)
                print("Barbara's -", barbara_count, "\n")
                time.sleep(0.2)
                print("Shogun's -", shogun_count, "\n")
                time.sleep(4)


            else:
                print("Invalid")

        running = False

    pygame.quit()

main_gacha()
