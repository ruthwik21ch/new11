def remove_common_letters(name1, name2):
    name1 = list(name1)
    name2 = list(name2)
    for ch in name1[:]:  # iterate over a copy
        if ch in name2:
            name1.remove(ch)
            name2.remove(ch)
    return len(name1) + len(name2)

def flames_result(count):
    flames = list("FLAMES")
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:-1]
    return flames[0]

def get_flames_meaning(letter):
    return {
        'F': "Friends",
        'L': "Love",
        'A': "Affection",
        'M': "Marriage",
        'E': "Enemy",
        'S': "Siblings"
    }[letter]

def highlight_flames(result_letter):
    flames = "FLAMES"
    highlighted = ""
    for ch in flames:
        if ch == result_letter:
            # Green text highlight
            highlighted += f"\033[92m{ch}\033[0m "
        else:
            highlighted += f"{ch} "
    return highlighted.strip()

def main():
    boy = input("Enter the boy's name: ").lower().replace(" ", "")
    girl = input("Enter the girl's name: ").lower().replace(" ", "")
    
    count = remove_common_letters(boy, girl)
    result_letter = flames_result(count)
    meaning = get_flames_meaning(result_letter)
    highlighted_flames = highlight_flames(result_letter)
    
    print("\nFLAMES Result Letters:")
    print(highlighted_flames)
    print(f"\n🔥 Result: {boy.title()} and {girl.title()} are '{meaning}'!")

if __name__ == "__main__":
    main()
