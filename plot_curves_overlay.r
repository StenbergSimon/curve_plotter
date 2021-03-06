for (package in c('ggplot2','grid', 'Rmisc', 'reshape2')) {
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
p <- ggplot(z, aes(x=X, y=value, fill=name))
p <- p + geom_line() + scale_y_continuous(trans="log2") + annotation_logticks(base=2, sides="l") + labs(x="Time", y="Cells (log2)") + theme_classic(base_size=15)
p <- p + geom_ribbon(aes(ymin=value-sd, ymax=value+sd), alpha=0.5)
p <- p + theme(legend.key.size = unit(1, "mm"), legend.text = element_text(size=3))+ guides(fill=guide_legend(ncol=2,title=""))
pdf(paste("summary",".pdf",sep=""))
print(p)
dev.off()
