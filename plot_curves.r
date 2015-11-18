for (package in c('ggplot2', 'Rmisc', 'reshape2')) {
    if (!require(package, character.only=T, quietly=T)) {
        install.packages(package, dependencies=TRUE)
        library(package, character.only=T)
    }
}

args<-commandArgs(TRUE)

filename = args[1]

x <- read.csv(filename)
x.molten <- melt(x, id.vars="X")
x.sum <- summarySE(data=x.molten, groupvars="X", na.rm=TRUE, measurevar="value")
p <- ggplot(x.sum, aes(x=X, y=value))
p <- p + geom_line(color="purple") + geom_ribbon(fill="purple", aes(ymin=value-sd, ymax=value+sd), alpha=0.5) + scale_y_continuous(trans="log2") + annotation_logticks(base=2, sides="l") + labs(x="Time", y="Cells (log2)") + theme_classic(base_size=15) + ggtitle(filename)
pdf(paste(filename,".pdf",sep=""))
print(p)
dev.off()
