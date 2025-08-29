// This code uses the Random class to generate a random number between 1 and 6, simulating a dice roll.

import java.util.Random;

public class Dice {
    public static void main(String[] args) {
        Random random = new Random();
        int diceRoll = random.nextInt(6) + 1; // Generates a number between 1 and 6
        System.out.println("You rolled a " + diceRoll);
    }
}
