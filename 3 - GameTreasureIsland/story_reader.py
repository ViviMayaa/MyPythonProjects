def story_reader():
    with open("Story", "r") as story_draft:
        story_list = [[]]
        i = 0
        for element in story_draft.read():
            story_list[i] += element
            if element == "\\":
                story_list[i].remove("\\")
                story_list.append([])
                i += 1
    # print(story_list)

    # for element in story_list[0]:
    #     print(element, end = "")
    return story_list
