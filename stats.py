def get_num_words(text):
    words=text.split()
    return len(words) 


def char_count(text):
    dict={}
    for i in text:
        if i.lower() not in dict:
            dict[i.lower()]=1
        else:
            dict[i.lower()]+=1
    return dict
        
        
def sort_on(items):
    return items["num"]       
        
def sort_char_count(char_count_dict):
    sorted_list =[]
    for i in char_count_dict:
        sorted_list.append({"char": i,"num":char_count_dict[i]})
        
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list