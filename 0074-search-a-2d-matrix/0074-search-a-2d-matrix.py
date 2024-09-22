class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1

        while (left <= right):
            middle = left + ((right - left) // 2)
            if matrix[middle][len(matrix[middle])-1] < target:
                left = middle + 1
            elif matrix[middle][0] > target:
                right = middle - 1
            else:
                m_left, m_right = 0, len(matrix[middle])-1
                while (m_left <= m_right):
                    m_middle = m_left + ((m_right - m_left) // 2)
                    if matrix[middle][m_middle] < target:
                        m_left = m_middle + 1
                    elif matrix[middle][m_middle] > target:
                        m_right = m_middle - 1
                    else:
                        return True
                return False
        return False