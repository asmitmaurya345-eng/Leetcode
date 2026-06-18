class Solution(object):
    def angleClock(self, hour, minutes):
        h_angle=30*hour+0.5*minutes
        m_angle=6*minutes
        angle=(h_angle-m_angle)
        angle_=abs(angle)
        max_angle=min(angle_,360-angle_)
        return max_angle