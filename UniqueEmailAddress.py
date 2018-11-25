class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # 1. Anything after + and before @ should be ignored
        # 2. '.' must be ignored
        result = set()
        if emails is None:
            return emails
        for email in emails:
            if email is None or len(email) == 0:
                return email
            else:
                result.add(self.handleSingleEmail(email))
        return len(result)

    def handleSingleEmail(self, email):
        plus_index = email.find('+')

        if plus_index != -1:
            at_index = email.find('@')
            email = email[0: plus_index] + email[at_index:]
        at_index = email.find('@')
        while email.find('.') != -1 and email.find('.') < at_index:
            dot_index = email.find('.')
            email = email[0: dot_index] + email[dot_index + 1:]
        return email


if __name__ == '__main__':
    s = Solution()
    print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))