for (package in c('ggplot2', 'Rmisc', 'reshape2')) {
    if (!require(package, character.only=T, quietly=T)) {
        install.packages(package, dependencies=TRUE)
        library(package, character.only=T)
    }
}

args<-commandArgs(TRUE)

listfile = args[1]
z <-data.frame()
list<-read.csv(listfile)
for (name in rownames(list)){ x<-read.csv((as.character(as.factor(list[name,]))))
x.molten <- melt(x, id.vars="X")
x.molten$name <- as.character(as.factor(list[name,]))
x.sum <- summarySE(data=x.molten, groupvars=c("X", "name"), na.rm=TRUE, measurevar="value")
z <- rbind(z,x.sum)}

#z.sum <- summarySE(data=z, groupvars=c("X","variable") , na.rm=TRUE, measurevar="value")
p <- ggplot(z, aes(x=X, y=value, color=name))
p <- p + geom_line() + scale_y_continuous(trans="log2") + annotation_logticks(base=2, sides="l") + labs(x="Time", y="Cells (log2)") + theme_classic(base_size=15) + theme(legend.position="none")
pdf(paste("summary",".pdf",sep=""))
print(p)
dev.off()
