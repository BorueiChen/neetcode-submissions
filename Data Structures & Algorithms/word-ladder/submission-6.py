class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adj = {}
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                if pattern not in adj:
                    adj[pattern] = [word]
                else:
                    adj[pattern].append(word)

        queue = deque([beginWord])
        visited = set([beginWord])
        step = 1
        while queue:
            print(f"step: {step}, queue:{queue}, visit: {visited}")
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for neighbor in adj.get(pattern, []):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            step += 1
        return 0