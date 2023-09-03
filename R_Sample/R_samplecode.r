par(family = "HiraKakuProN-W3")

tickValues <- c(0,0.5,1) # 自動で区分け
tickStrings <- sprintf("%s",c("0%","50%","100%")) 

plot(dbinom(seq(0,2,by=1),2,0.5),
     ylim=c(0,1),
     xaxt="n",yaxt="n",
     xlab="表が出る回数",
     ylab="確率",pch=20,
     main="コインを２回投げたときのX")
axis(side=1, at=1:3, labels=0:2)
axis(side=2, at=tickValues, labels=tickStrings)