def levelOrder(self):

  traversal = ""
  l= list()
  t = self.root
  l.append(t)

  while(len(l)!=0):
   traversal += (str(l[0].data) + " ")
   if l[0].left:
    l.append(l[0].left)
   if l[0].right:
    l.append(l[0].right)
   l.remove(l[0])
  return traversal

print(levelOrder())