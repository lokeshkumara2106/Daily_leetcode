class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # d={}
        # for i,c in enumerate(s):
        #     if c not in d:
        #         d[c]=[-1,-1]
        #         d[c][0]=i
        #         d[c][1]=i
        #     else:
        #         d[c][1]=i
        # sor=sorted(d.values(), key=lambda x:x[0])
        # m=sor[0][1]
        # res=[]
        # for x in range(1,len(sor)):
        #     if sor[x][0]>m:
        #         if res:
        #             res.append(m-sum(res)+1)
        #         else:
        #             res.append(m+1)
        #         m=sor[x][1]
        #     m=max(m,sor[x][1])
        # res.append(m-sum(res)+1)
        # return res

        d={}
        for i,c in enumerate(s):
            if c not in d:
                d[c]=[i,i]
            else:
                d[c][1]=i
        vals=sorted(d.values(),key=lambda x:x[0])
        l=[vals[0]]
        for x,y in vals[1:]:
            if l[-1][1]>x:
                l[-1][1]=max(l[-1][1],y)
            else:
                l.append([x,y])
        return [y-x+1 for x,y in l]