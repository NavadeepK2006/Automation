Project Title:- Automated Book Publication Workflow

A. What This Project Is About:- This project is designed to automatically take a chapter from an online book, rewrite it using AI, review it again with another AI step, and then let a human give feedback using their voice. The goal is to combine automation and human creativity to make content better, step by step.

B. What I Did?
1. First, I made the system scrape a public domain chapter from Wikisource using a tool called Playwright. It fetches the full content and also takes a screenshot of the original page.

2. Then, I connected an AI model to rewrite the chapter in a slightly different way — like how a writer would paraphrase a story. After that, another AI model acts as a reviewer and refines the content to make sure it sounds clean and consistent.

3. Now comes the cool part. I added voice support. The AI reads out the final version, and I (or any user) can say "yes" to approve or "no" to suggest changes. If the user says "no", the system listens again so you can speak your improvements aloud. It's like talking to a real editor.

4. After the user approves a version, it’s saved with version control using something called ChromaDB. That helps keep track of all changes and makes it easy to search older versions semantically — meaning by the actual meaning, not just keywords.

5. There's also a reinforcement logic behind the scenes. Based on whether I accept or reject the AI’s version, it adjusts the "reward", which later helps to understand which versions are more useful.

C. Tools I Used:-
1. Python for building the full system
2. Playwright for web scraping
3. AI models (like OpenAI or Gemini) for writing and reviewing
4. Pyttsx3 and SpeechRecognition for voice support
5. ChromaDB for version storage and smart search
6. RL logic for learning from feedback

D. Why This Matters:- In a real publishing environment, editors go through multiple rounds with writers. This project mimics that — except with AI helping at every stage and voice being used to make feedback natural and quick.

E. How You Can Run This:-
If you want to try it yourself:
1. Install the required libraries
2. Make sure your mic is working and Playwright is installed
3. Run the main file and just speak when prompted
4. Your responses will control the process