class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplifies a given Unix-style file path by resolving any ".." and "." components.

        Args:
        - path (str): A string representing a Unix-style file path. The path can contain the following components:
            - A leading forward slash (/), indicating the root directory.
            - Zero or more directory names, separated by forward slashes (/).
            - Special components:
                - An empty string, representing the current directory.
                - A single dot (.), also representing the current directory.
                - Two dots (..), representing the parent directory.

        Returns:
        - A string representing the simplified path, with the following rules applied:
            - Any leading or trailing slashes are removed.
            - Any empty or single-dot components are ignored.
            - Any double-dot components are resolved by removing the last directory name from the stack of directories, if it is non-empty.
            - If the resulting stack of directories is empty, a single forward slash is returned to represent the root directory.
            - Otherwise, the directories are joined with forward slashes and a leading slash is added.

        Example:
        - Input: "/a/./b/../../c/"
        Output: "/c"
    """
        stack = []

        for str in path.split('/'):
            if str in ('', '.'):
                continue
            if str == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(str)

        return '/' + '/'.join(stack)

## 71. Simplify Path