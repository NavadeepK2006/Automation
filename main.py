from config import WIKISOURCE_URL,SCREENSHOT_PATH
from scraping.scraper import fetch_chapter
from ai_agents.ai_writer import spin_content
from ai_agents.ai_reviewer import review_text
from ai_agents.rl_reward import calculate_reward
from human_loop.iteration import human_feedback_loop
from versioning.chroma_manager import add_version
from utils.logger import log
def main():
    log("Fetching original content...")
    original=fetch_chapter(WIKISOURCE_URL,SCREENSHOT_PATH)
    log("Running AI Writer...")
    spun=spin_content(original)
    log("Running AI Reviewer...")
    reviewed=review_text(spun)
    reward=calculate_reward(spun, reviewed)
    log(f"RL Reward: {reward}")
    log("Starting human feedback loop with voice interaction...")
    final_version,approved=human_feedback_loop(reviewed)
    if approved:
        doc_id="chapter1-final"
        add_version(doc_id,final_version)
        log(f"Saved final version with ID: {doc_id}")
    else:
        log("Final version not approved.")
if __name__ == "__main__":
    main()