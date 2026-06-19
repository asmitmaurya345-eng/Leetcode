class Solution(object):
    def largestAltitude(self, gain):
        altitude=0
        a_list=[0]
        for x in gain:
            altitude+=x
            a_list.append(altitude)
        return max(a_list)