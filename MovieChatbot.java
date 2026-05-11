import java.util.Scanner;

public class MovieChatbot {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Welcome to MovieBot 🎬");
        System.out.println("Ask me about movies like action, comedy, horror, or ratings!");

        while (true) {
            System.out.print("\nYou: ");
            String userInput = sc.nextLine().toLowerCase();

            if (userInput.contains("action")) {
                System.out.println("Chatbot: You can watch Avengers, John Wick, or Mission Impossible.");
            }
            else if (userInput.contains("comedy")) {
                System.out.println("Chatbot: Try The Mask, Mr. Bean, or Hangover.");
            }
            else if (userInput.contains("horror")) {
                System.out.println("Chatbot: You might like The Conjuring, It, or Annabelle.");
            }   
            else if (userInput.contains("rating")) {
                System.out.println("Chatbot: Most popular movies have ratings above 7/10 on IMDb.");
            }
            else if (userInput.contains("latest")) {
                System.out.println("Chatbot: Latest movies include new releases in theatres and OTT platforms.");
            }
            else if (userInput.contains("time") || userInput.contains("duration")) {
                System.out.println("Chatbot: Most movies are around 2 to 3 hours long.");
            }
            else if (userInput.contains("hello") || userInput.contains("hi")) {
                System.out.println("Chatbot: Hello! What kind of movie do you want?");
            }
            else if (userInput.contains("bye") || userInput.contains("exit") || userInput.contains("quit")) {
                System.out.println("Chatbot: Goodbye! Enjoy your movie time 🍿");
                break;
            }
            else {
                System.out.println("Chatbot: Sorry, I didn't understand. Try asking about movie genres!");
            }
        }

        sc.close();
    }
}
