from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) > maxWidth:
                result.append(self.format_line(current_line, maxWidth, False))
                current_line = []
                current_length = 0

            current_line.append(word)
            current_length += len(word)

        result.append(self.format_line(current_line, maxWidth, True))

        return result

    def format_line(self, words, maxWidth, is_last_line):
        spaces_to_add = maxWidth - sum(len(word) for word in words)
        word_count = len(words)

        if word_count == 1 or is_last_line:
            return ' '.join(words) + ' ' * (maxWidth - len(' '.join(words)))

        spaces_between_words = spaces_to_add // (word_count - 1)
        extra_spaces = spaces_to_add % (word_count - 1)

        formatted_line = words[0]
        for i in range(1, word_count):
            if i <= extra_spaces:
                formatted_line += ' ' * (spaces_between_words + 1)
            else:
                formatted_line += ' ' * spaces_between_words
            formatted_line += words[i]

        return formatted_line
