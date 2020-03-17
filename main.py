import sys

max_len = 26  
def string_map(string1, string2):  
    l1 = len(string1) 
    l2 = len(string2)
    if (l1 != l2): 
        return False
    freq_s1 = [0 for i in range(max_len)] 
    freq_s2 = [0 for i in range(max_len)] 
    for i in range(l1): 
        freq_s1[ord(string1[i]) - ord('a')] += 1
    for i in range(l2): 
        freq_s2[ord(string2[i]) - ord('a')] += 1
    for i in range(max_len):  
        if (freq_s1[i] == 0): 
            continue
        found = False
        for j in range(max_len): 
            if (freq_s1[i] == freq_s2[j]): 
                freq_s2[j] = -1 
                found = True
                break 
        if (found==False): 
            return False
    return True

if __name__ == '__main__': 
    s1 = sys.argv[1]
    s2 = sys.argv[2] 
    print(string_map(s1, s2))