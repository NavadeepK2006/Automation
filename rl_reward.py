def calculate_reward(original,reviewed):
    """
    Simulated RL reward function: +1 if more concise, else -1
    """
    if len(reviewed.split()) < len(original.split()):
        return 1
    return -1