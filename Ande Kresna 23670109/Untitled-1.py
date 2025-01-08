def backtrack(state):
    if is_solution(state):
        save_solution(state)
    else:
        for child in generate_children(state):
            if is_valid(child):
                backtrack(child)
