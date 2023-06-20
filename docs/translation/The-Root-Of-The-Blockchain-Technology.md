# 共识算法：区块链技术的根源

> 本文的原文为[Consensus Algorithms: The Root Of The Blockchain Technology](https://101blockchains.com/consensus-algorithms-blockchain/)，转载自[101blockchains](https://101blockchains.com)，作者是Hasib Anwar。

> 本文为原文的中文翻译，属个人翻译作品，翻译不到之处还请指正。也感谢Hasib Anwar写的文章，这对了解区块链共识算法有很大的帮助。

## 引言

每一天，我们都可以看到新的区块链技术出现在我们生活当中。无论我们如何努力想要掌握最新的技术，却总是应接不暇。有没有想过所有这些区块链技术的根源是什么呢？好吧，共识算法是这些革命性技术的首要根源。

共识算法使得所有这些区块链共识序列不同于其他的算法。在同一个地方，区块链网络便利了成千上百万的人们。那么，为什么它们永远不会相互干预或者相互存在呢？

答案就在区块链网络的架构里。该架构设计巧妙，并且共识算法在该架构的最核心位置。

如果你真的想知道区块链共识序列是如何工作的，那么你必须要比你所想的更为深入。这也就是为什么我将在本指南中涵盖所有已知的共识算法的内容了。那么，让我们继续吧！

## 目录

- [第一章：什么是共识算法？](#第一章：什么是共识算法？)

- [第二章：拜占庭容错算法的问题](#第二章：拜占庭容错算法的问题)

- [第三章：我们为什么需要共识算法？](#第三章：我们为什么需要共识算法？)

- [第四章：区块链：分布式网络中有组织的数据的框架](#第四章：区块链：分布式网络中有组织的数据的框架)

- [第五章：共识算法：网络的灵魂](#第五章：共识算法：网络的灵魂)

- [第六章：不同类型的共识算法](#第六章：不同类型的共识算法)
  
- [第七章：其他类型的共识算法](#第七章：其他类型的共识算法)

- [第八章：结论](#第八章：结论)



## 第一章：什么是共识算法？

技术定义可能是这样的：

共识算法是一个组的决策过程，组中的个体构建并支持最适合组中其余个体的决策。这是一种解决方案，个体需要支持多数决策，无论它们是否喜欢。

简单来讲，它就是一种组内决策的方法。我举一个例子你就明白了。想象一个有10个人的小组，想要就项目于他们个人的利益做一个决定。每个人都可以提出一个想法，但是大多数将同意其中的一个最为有用的想法，而其他人必须接受这个决定，无论他们喜欢与否。

现在想象下这样的一个决定对1000个人的小组来说是什么样的情况。难道这不会使得决策变得更加艰难吗？

共识算法不仅仅是赞同大多数的投票，而且还要同意对全体都有利的那个。因此，它总会在网络中取胜。

区块链共识模型是在互联网世界里创造公平和公正的一种方法。用于这种协定的共识系统我们称其为共识定理。

这些区块链共识模型由一些特殊的对象组成，例如：

- 达成协议：该机制尽可能多的收集组内的所有协议。

- 协作：小组成员都希望达成更好的协议，以此产生对整个小组更好的利益。

- 合作：每个个体都将团结一致，而把自己的利益放在一边。

- 平等权利：每个参与者在投票中都有相同的价值，这意味着每个人的投票都很重要。

- 参与：每个在网络中的个体都需要参与投票。不会有人将被遗漏，更不会有人可以不投票就留在外面。

- 活动：小组中的每个成员都同样活跃，没有哪个成员将负有更多的责任。

**Different Types of Consensus Algorithms Infographic**

![Different Types of Consensus Algorithms Infographic](https://github.com/i0Ek3/GetYourPaper/blob/master/image/Different_Consensus_Algorithms.png)



## 第二章：拜占庭容错算法的问题

拜占庭容错是一种具有特定故障时间的系统，它被称为拜占庭将军问题，你可以通过分布式计算机系统来更好地体验这种情形。很多时候，共识系统可能会出现故障。

这些组件将进一步解决冲突的信息，只要所有要素协调一致，共识系统才能成功地运行。然而，如果系统中的一个组件出现故障，则整个系统将会发生故障。

故障成分总是会导致拜占庭容错系统不一致，这也就是为什么它对于使用共识算法的去中心化网络而言不是理想的。

专家们称它为“拜占庭将军问题”，仍然疑惑吗？

让我用一个共识的例子来讲清楚它。

想象一下这里有一组将军，他们每个人都拥有一支拜占庭军队。他们准备去攻占一个城邦，并且他们需要决定如何展开攻击。

你可能认为这很轻松。然而，却有一点点困难。将军们只可以通过信使来沟通，并且这里有些叛徒将军试图破坏整个攻击。

他们可以通过信使来发送不可靠消息，或者信使也可以成为叛徒。

信使也可以通过传送错误的消息来故意搞破坏。

这就是为什么这个问题需要被谨慎处理了。首先，无论如何我们都需要将军们互相达成决定。第二，确保即使是最少的叛徒数量也不会使的整个任务失败。

这对你来说可能相当简单，然而，并不是这样。根据研究，在有n个叛徒的将军中，需要有3n+1个将军是诚实的。也就是说，需要有4名将军来对应一个叛徒，这的确有些棘手。



## 第三章：我们为什么需要共识算法？

拜占庭主要的问题是达成协议。如果出现单点故障，则所有节点无法达成协议或者获得一个更高的难度值。

另一方面，共识算法并不真正面对这类问题。他们的主要目标是以任何方式达到特定的目的。区块链共识算法模型是比拜占庭更可信任和更具容错性的。

这就是为什么在分布式系统中会有矛盾的结果，而用一致性算法便是为了有一个更好的输出。



## 第四章：区块链：分布式网络中有组织的数据的框架

现在让我们来窥探一下区块链技术，以便更好地了解整个网络。

* 它是组织数据库的一种新方法。
* 它可以存储根据网络变化的所有内容。
* 所有数据就像物品一样整齐的排列在块中。

然而，你却无法在区块链本身上看到任何去中心化。这是因为区块链并不提供去中心化的环境。这就是我们需要共识算法来使得系统变得去中心化的原因了。

所以，区块链技术只允许你创建一个不同的结构化数据库，但是它并不执行去中心化进程。这就是为什么区块链被认为是整个去中心化网络里的骨架了。


## 第五章：共识算法：网络的灵魂

方法是真的很简单。这些区块链共识模型仅仅是达成协议的方式。但是，如果没有共同的共识算法，就不可能有任何的去中心化系统。

它甚至不需要在意节点之间是否会彼此信任。他们必须遵守确定的规则并且来达成集体协议。为此，你必须检查所有的共识算法。

目前，我们还没有发现任何适用于每种区块链技术的特定区块链算法。让我们见识一下不同的区块链共识算法，以便更好地了解整个情况。



## 第六章：不同类型的共识算法

原文列出的共识算法：

* PoW--工作量证明
* PoS--股权证明
* DPoS--委托股权证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/058.pdf)
* LPoS--租赁股权证明
* PoET--时间消逝证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/062.pdf)
* PBFT--实用拜占庭容错
* SBFT--简单拜占庭容错
* DBFT--委托拜占庭容错
* DAG--有向无环图
* PoA--活动证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/064.pdf)
* PoI--重要性证明
* PoCapcity--容量证明
* PoB--燃烧证明
* PoWeight--权值证明

笔者列出的共识算法：

* Bitcoin-NG
* Casper
* Tendermint
* Raft [动画演示](http://thesecretlivesofdata.com/raft/)
* Paxos
* PoL--幸运证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/030.pdf)
* PoP--可能性证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/035.pdf)
* PoV--投票证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/052.pdf)
* PoT--信任证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/056.pdf)
* PoContribution--贡献证明 [参考](https://github.com/i0Ek3/YGP/blob/master/paper/blockchain/057.pdf)
        

### Proof of Work

工作量证明是第一个在区块链网络中被引用的区块链共识算法。许多区块链技术使用该区块链共识模型来确认他们的所有交易并为网络链生成相关的区块。

去中心化的账本系统在区块中收集所有相关的信息。但是，需要特别关注事务块。

这个责任落在称为矿工的单个节点上，而矿工所维护的这一过程我们称之为挖矿。该技术背后的核心原则是为了解决复杂的数学难题并给出结果。
	
你可能在想是什么样的数学难题呢？

这些数学难题需要大量的计算机算力才能开始。例如，哈希函数或者已知如何在没有输入的情况下找到输出。另一个是整数分解，它也涵盖了旅游难题。

当服务器感觉被DDoS攻击并且发现共识系统需要的大量计算时，便会发生这样的情况，这就是矿工需要做的。整个数学方程问题的答案我们称之为哈希解谜。

但是工作量证明有一定的限制。网络似乎增长了很多，因此，它需要大量的计算能力。该过程使得系统变得缓慢。

![PoW](https://github.com/i0Ek3/GetYourPaper/blob/master/image/PoW.png)


#### 为什么系统会变得如此敏感呢？

区块链共识序列主要依赖准确的计算数据和信息。但是，系统的速度却跟不上。如果问题变得太过复杂，则生成块需要花费大量的时间。

交易延迟了，所有的工作流便会暂停。如果在特定时间内无法解决块生成的问题，那么生成一个区块将变得困难。

但是，对一个系统来说，若是问题变得太简单，它将更容易受到DDoS攻击。此外，需要进一步精确地检查解决方案，因为并不是所有的节点都可以检查可能的错误。

如果他们可以，网络将缺乏最为重要的特质--透明性。


#### 工作量证明机制是如何在区块链网络上实现的？   

首先，矿工将会解决所有的谜题，之后将创建新的区块并在此之后来确认交易。无法说出谜题有多么复杂。

它在很大程度上取决于最大用户数，最小电流功率和网络总负载。

新的区块带有哈希值，并且每个区块都包含着前一个区块的哈希值。通过这种方式，网络添加了额外的防护层并防止任何类型的侵犯。一旦矿工解决了谜题，一个新的区块将被创建，交易也将被确认。


#### 区块链中在哪里确切地用到了工作量证明共识算法？

最流行的便是比特币了。比特币在任何其他加密货币之前便引用了这种共识算法。区块链共识模型允许基于网络的整体功能对谜题的难度进行任何类型的更改。

创建新的区块大约需要花费10分钟。类似莱特币的其他加密货币也提供了同样的机制。

另一个区块链算法用户，以太坊，在平台上的近3-4个大型项目中使用了工作量证明。然而，以太坊已经转向了股权证明。


#### 为什么区块链技术首先使用工作量证明？

你一定会好奇为什么不同的区块链技术首先使用工作量证明。

这是因为工作量证明提供DDoS防护并降低了整个股权开采。该区块链算法为黑客们提供了相当大的难度。该系统需要大量的算力和效率。

这也是黑客入侵区块链共识模型的原因所在了，但是它的代价很高，可能需要花费较长的时间和复杂度。

另一方面，没有矿工可以决定整个网络，那是因为决策并不依赖金钱的数量。而是依赖你有多少算力可以形成新的区块。


#### PoW共识算法的主要问题是什么？

不是所有的共识算法都是完美的；PoW也是不完美的，它有很多好处也有很多的缺陷。让我们来看看系统中的主要缺陷是什么。

* **巨大的能量消耗**

区块链网络包含了成千上万的哈希常用的微芯片，这个过程需要大量的电力。

目前比特币每秒可以提供200亿个哈希值。网络上的矿工使用一些特殊设计的微芯片进行哈希计算。该过程允许网络添加防护层来免受僵尸网络的攻击。

区块链网络的安全等级是基于需要大量能量的PoW共识机制，并且是密集的。巨大的消耗成为现实世界的一个问题，系统中的矿工需要承受巨大的电力消耗成本。

而这个问题的最好的解决办法便是廉价的能源。


* **矿工集中化**

随着能源问题，PoW将选择更便宜的电力解决方案。然而，主要的问题是比特币矿工制造商在不断地增加。在一定时间内，制造商可能变得更加耗电并试图在挖矿系统中创建新的规则。

该解决方案在去中心化的网络中将变得集中化。这就是区块链算法面临的另一个严峻问题的原因了。


#### 51%算力攻击为何物？

让我来解释清楚51%攻击真正的含义。该攻击意味着攻击者可能会控制大部分用户并且占有大量的挖矿能源。在这个场景中，攻击者将有足够的能源来控制网络中的一切。

他们可以阻止其他人生成区块。攻击者也可以接受基于他们把戏的奖励。

让我来举一个共识的例子。

想象一下这样的一个场景：爱丽丝通过区块链网络给鲍勃转账了一些加密货币。但是爱丽丝受到了攻击，而鲍勃并没有。交易被取代，但是攻击者并不会通过在链中启动分叉来转移任何金额的资金。

另外一种情况是，矿工将加入其中一个分支。他们将主要的算力结合到这些区块上。这就是为什么其他寿命较短的区块被拒绝的原因。最后，鲍勃并没有收到钱。

但是，这并不是有利可图的解决办法。因为这需要很大的挖矿能源，并且如果事件被曝光后，用户将永久地离开网络，而交易成本将会下降。


### PoS

#### 什么是PoS？

PoS是一种可以解决PoW算法主要缺陷的区块链共识算法。在该算法中，每个区块在加入区块链账本中之前会验证区块。矿工可以用它们金币的股权来加入挖矿进程。

PoS是一种新的概念，每个个体可以基于它们所拥有的币进行挖矿或者验证区块。因此，在这个场景中，你有越多的金币，你的机会也就越多。


#### 它是如何工作的？

在这个共识算法中，矿工可以获得之前地选择。

尽管整个过程是随机的，但也并不是每个矿工可以参与赌注。网络中所有的矿工随机地被选择。如有你的钱包里之前有存储一定数量的金币，那么你将有资格成为网络中的一个节点。

在成为一个节点之后，如果你想要有资格成为一名矿工，你将需要存入一定数目的金币，在那之后会有一个投票系统来选择验证者。当这些事情全部完成后，矿工将获得特定钱包赌注所需的最低金额。

该过程相当的简单。将根据钱包与硬币数量成比例地创建新的区块。例如，如果你拥有10%的金币，那么你可以挖出10%的新区块。

有很多区块链技术中应用了PoS共识算法。但是，对于挖掘一个新的区块来说，所有的共识算法的工作方式都是一样的，即每个矿工将会获得区块奖励以及交易费用的一部分。

![PoS](https://github.com/i0Ek3/GetYourPaper/blob/master/image/PoS.png)


#### 在PoS矿池中发生了什么？

有许多其他方式来参与赌注。如果赌注的数量非常大，那么你可以加入一个矿池并通过此来挣取利润。有两种方式可以做到。

首先，你可以把你的金币贷款给另一个已经加入矿池的用户，之后他可以与你分享利润。但是，你需要找到一个可信的人。

另一种方式是你自己加入到矿池中去。在这种方式下，参与该特定的矿池的每个人都将基于股权的数量来划分利润。


#### PoS：有什么好处？

首先，这种类型的共识算法不需要任何大量的硬件备份。你只需要有一个功能强大的计算机系统和一个稳定的网络即可。任何在网络上拥有足够金币的人都可以验证交易。

如果一个人投资于网络，它将不会像其他投资一样随着时间而贬值。唯一会影响利润的是价格浮动。PoS共识算法较PoW而言更为节能。它甚至不需要太多的电力消耗。

它也减少了51%攻击的威胁。

尽管PoS看起来比PoW更有利可图，但它仍然有非常严重的缺点。系统中主要的缺陷是永远不可能完全去中心化。

这是因为只有少数节点参与了网络上的赌注，拥有最多金币的个体最终会控制大部分系统。

![PoW VS PoS](https://github.com/i0Ek3/GetYourPaper/blob/master/image/PoW-vs-Pos-Simply-Explained.png?1538298537503)


### 利用股权证明作为区块链技术基础的流行加密货币

#### PIVX

这是另一个隐私货币，几乎没有交易费用。PIVX以前是从Dash分叉的。但是，它从PoW转到了PoS。它们还通过使用主节点来分发区块以此确保更好的参与赌注。

如果你想开始使用PIVX，你需要下载官方的钱包并且同步区块链中的数据。在这之后，你可以向钱包里转入一些金币，然后将其保持连接状态。


#### NavCoin

许多加密货币都是分叉自比特币的原始区块链共识序列，NavCoin就是其中之一。该项目完全开源。他们比大多数的加密货币更早的转移到PoS中去。

为了获得最大的利益，你的电脑需要长时间的连接网络。PoS十分轻巧，你可以毫无担心的让它自己长时间的运行。


#### Stratis

这是运行PoS的另一个区块链共识序列。这些服务主要面向企业。公司可以使用它来构建自己的dApp，而无需拥有自己的区块链网络。

该平台提供侧链中app的开发，可防止任何类型的网络延迟。他们开始于PoW项目，但是，最终他们转向了PoS。


### 区块链算法：委托股权证明共识 DPoS

委托股权证明是典型的股权证明的变体。其拥有健壮的系统，并且在整个等式中加入了不同形式的灵活度。

如果你想要快速、高效、去中心化的共识算法，那么委托股权证明是最好的方式。股东的问题在民主方面得到了充分的解决。网络上的所有成分都可以成为代理。

在该共识机制中，不同于矿工和验证者，所有的节点都叫委托者。通过确定块的生成，该系统可以在一分钟内就可以完成交易。而且，该系统旨在确保针对监管问题提供各种级别的保护。


#### 证人验证所有签名

通常，证人不受法规和其他中立的约束。传统合同中的标准证人有证人作证的特殊地方。它们只是确保个人应该在指定时间接触。

在DPoS中，证人可以生成信息块。还有投票选举最高证人的概念。投票仅会在系统完全去中心化的情况下发生。

所有证人在生成一个块后立即获得报酬，而费率是在之前通过投票系统选择好的。


#### 选举代表中的特殊参数变更

同证人一样，代理也会被选中。代理们用于全面更改网络的参数。对于代理来说，它们可以获得交易费用，块间隔，块大小和证人的支付。

为了更改网络中的参数，大多数代理需要为同一件事物进行投票。但是，代理不会像证人那样获得报酬。


#### 改变典型的规则

为了平稳运行系统，必须要时刻增加不同的特性。但是，增加特性的过程不会在没有股东的情况下完成。证人可以一起更改政策，但是它们无法通过编程来实现。

它们需要保持中立并且仅有股东的雇员才可以这样做。因此，最初，所有的事情都需要依赖于股东。


#### 双花攻击的风险

在DPoS中，双花的风险在很大程度上已经降低了。当区块链网络未能在数据库中包含先前花费的事务时，可能会发生这种情况。

网络可以在没有任何人帮助的情况下检查该交易是否正常，并且可以探测任何类型的损失。在这种方式下，它可以保证数据库100%透明。


#### 交易作为股权证明

虽然系统是股权证明的变体，但核心交易系统仍然完全依靠股权证明运行。股权证明的交易过程可以确保已经增加了应对错误共识系统的防护层。


#### 谁在使用DPoS？

Lisk在市场中是非常流行的名字。该区块链平台为开发者们提供一个平台，可以毫不费力的进行基于JavaScript的去中心化应用开发。

它同以太坊有很多共同的元素。但是，系统使用DPoS代替了PoS。

其中，参与赌注的方式也与此不同。


### LPoS

经典的PoS的另一个转折点是LPoS--租赁股权证明。新的区块链共识算法被引入到我们的Waves平台。就像其他区块链技术平台一样，Waves平台确保以有限的功耗提供更好的挖矿。

最初的PoS对参与赌注有一些限制。拥有有限数量金币的个人可能永远不会真正参与赌注。为了成功维护网络，只留下少数拥有更多金币的个人。

该过程允许系统在去中心化平台上创建中心化社区，显然这并不是我们所期望的。

在LPoS中，小的股东最终可以获得它们赌注的机会。它们可以租借它们的金币给网络并从中获益。

在引入新的LPoS之后，状况完全变了。现在可以毫不费力的解决先前系统的限制了。Waves平台的主要目的便是帮助那些小型投资者。

钱包里有少量金币的人永远不会有机会获得更大的好处。这样就完全确立了共识算法的主题--透明性。


### PoET

PoET是最好的共识算法之一。该特定的算法主要用于许可区块链，你需要获取访问网络的权限。这些有权限的网络需要来决定采矿权和投票原则。

为了确保一切顺利，PoET算法使用特定的策略来处理整个网络的透明性。共识算法也确保可以安全登录系统，因为在加入到矿工行列之前需要认证。

毋庸置疑，该共识算法有机会仅用公平的方式挑选获胜者。

让我们看看这个非常棒的共识序列的主要策略是什么。

* 每个人在网络上都需要等待一定的时间，但是对于时间的限制完全是随机的。
* 当参与者完成它所分配的随机等待时间便可以在账本上创建一个新的区块了。

为了验证这些场景的合理性，该共识算法需要考虑两个因素。

* 获胜者是否真的选择了随机数？TA可以选择一个随机短时间来获胜。
* 个人是否真的等待了所分配的特定时间吗？

PoET依赖特定的CPU，称为因特尔软件防护扩展SGX。该SGX有助于在网络中运行独特的代码。PoET使用该系统来确保获胜是公平的。


#### 因特尔SGX系统

正如共识算法使用SGX系统来验证选择的公平性，让我们更深入的研究一下该系统。

首先，特殊的硬件系统为使用特定可信代码创建一个证明，代码在安全的环境中设置。任何拓展的部分都可以使用该证明来验证它是否被篡改。

其次，代码运行在网络上无法进行交互的单独区域。

第一步是必需的，它将证明你在网络上是真的在使用可信代码而不是其他的什么随机技巧。如果第一步没有合适地运行，则可能永远无法找到主网络。

第二步阻止用户以TA以为运行的代码操纵系统，该步骤确保了算法的安全性。


#### 可信代码

让我们简化一下代码的轮廓。


##### 加入区块链网络

* 一个新用户首先在区块链中下载可信代码。
* 之后当TA开始该过程，它们会获得一个特殊的密钥对。
* 使用那个密钥对，用户可以发送SGX证明到网络并请求访问。


##### 参与彩票系统

个人将会从可信代码中获得签名计时器。

此后，个人将需要等待分配给他的时间完全消耗完毕。

最后，个人将会获得完成所需任务的认证。

该协议确保了基于SGX的不同等级的防护。该系统计算用户赢得彩票的次数。通过该方式，他们将知道个人用户的SGX是否履行了承诺。



### PBFT(实用拜占庭容错)

PBFT主要关注于状态机。它复制了系统但是摆脱了拜占庭将军的一般问题。那么，它是如何做的呢？

当然，该算法从一开始就假定网络中有可能存在故障，并且某些独立节点在某些时刻会发生故障。

该算法专为异步共识系统而设计，并以有效的方式进一步优化以解决所有问题。

而且，系统中的所有节点以特定的顺序排列着。选择一个节点作为主节点，其他的节点作为备份计划。但是，系统中的所有节点都协调工作并互相通信。

通信级别非常高，那是因为他们想要验证在网络上找到的所有信息。这样可以摆脱不可靠的信息问题。

但是，通过这个新过程，他们能够发现即使其中的一个节点受到损害。所有的节点通过多数的投票仍然可以达成协议。


#### PBFT共识算法的好处

实用拜占庭容错算法与我们分享了一些有趣的事实。该模型主要针对实际使用案例而设计，并且非常容易实现。因此，PBFT比其他共识算法具有一定的优势。

* 无需确认

在该网络上交易的工作方式有些许不同。如我们在PoW系统中看到的那样，它可以在没有任何类型的确认下就可以完成交易。

如果节点就特定的块达成一致，那么它将最终被确定。这是由于事实就是如此，所有真实的节点在同一时间同其他节点相互通信并了解特定块。

* 减少能源

与PoW相比，新的模型的功耗降低幅度更大。在PoW中，每一个区块都需要运行一定轮数。但是，在这个模型中，并不是每一个矿工都在解决典型的哈希算法。

这就是为什么系统不需要太多算力。


#### 系统的缺陷

尽管PBFT提供了许多优势和有前景的事实，但是其仍然会有许多劣势。让我们看看他们都是啥？

* 通信差距

该算法最重要的因素是节点之间的通信。网络上的所有节点必须确保他们所收集的信息是可靠的。但是，该共识算法仅适用于较小的节点组。

如果组中的节点在很大程度上增长，则系统可能会发现很难追踪所有的节点并且不能与它们中的每个节点通信。

本文支持这种模式状态，使用MAC和其他数字签名来证明信息的真实性。话虽如此，但MAC无法处理区块链类型的网络系统，因此，使用它最终可能成为重大的损失。

数字签名可能是一个好的点，但随着节点数量的增加，维护所有这些通信节点的安全性将变得越来越难。

* 女巫攻击

面对女巫攻击，PBFT是相当脆弱的。在这些攻击中，他们可以操控一组节点，并且如果这样做了，他们将会危及整个网络。对于更大的网络，这也会变得更糟，并且系统的可拓展性也会下降。

如果可以将此模型与另一种共识算法一起使用，那么他们可能会得到一个可靠安全组合。



### SBFT

在SBFT中，该系统的运行有点不同

首先，块生成器将在某个时刻收集所有的交易并在将他们合并到一个新类型的块之后验证他们。

简单来说，一个块将收集所有交易，它们批处理到另一个块中，最终在一起验证他们。

生成器应用所有节点遵循的某些规则来验证所有交易。之后，块签名者将验证他们并添加他们到自己的签名中。这就是为什么如果任何一个块错过了其中一个密钥后会被拒绝。

#### 简化拜占庭容错的不同阶段

* 该阶段从创建阶段开始，资产用户将生成更多数量的唯一资产ID。
* 之后，在提交阶段，用户在平台上提交所有的ID。
* 然后开始验证阶段，其中ID获得指定的用例条款。
* 一旦它们全部注册，他们将被存储并转移到不同的账户。交易可以在智能合约的帮助下进行。
* 最后，交易生效。

这个令人敬畏的系统的另一个很酷的特性是账户管理器，它可以在许多阶段给予帮助。其主要的目标就是安全的存储所有资产。账户管理器也存储所有的交易数据。管理器可以包含不同类型用户的所有的组合资产。

你可以认为这就是数字钱包。使用这些数字钱包，你将能够从钱包中转移资产，甚至可以接受别人转过来的资产。你也可以从智能合约中使用账户管理器，当满足特定需求时，它会释放资金。

但是资产的所有权是如何流动的呢？

好吧，事实上他们使用一个包含地址和资产ID推送模型来发送他们获得的资产。


#### 安全和隐私

SBFT用于网络中保密性占优先地位高的私有网络。该平台的设计是为揭露敏感信息，但存在一定的局限性。这就是系统使用三种技术的原因。例如零知识证明，一次性使用地址，加密元数据。

* 一次性使用地址

任何时刻用户想要从TA的钱包中接受一些资产时，系统将为他们分配一个临时使用地址。所安排的每个地址都不相同，因此，这阻止了任何用户想要拦截交易。

* 零知识证明

零知识证明用于隐藏所有交易的组成部分。但是，整个网络仍然能验证完整性。这可以在零知识证明的帮助下完成，其中一方向另一方证明它们的真实性。

在这种方式下，只有接收者和发送者才能看到交易的组成部分。

* 元数据加密

为了更进一步的保障安全性，交易的元数据会被加密。网络允许使用密钥来验证其真实性。但是，为了更好的保护，密钥将在2到3天更改一次。

而且，所有这些都保持分离状态，并且在数据网络的不同部分上。因此，如果它们其中一个被入侵，可以使用其他密钥来生成唯一的密钥。为确保这些共识算法的完整性，必须每隔几天管理和调整这些密钥。

Chain，是一个基于区块链的平台，它使用SBFT来验证网络上的所有交易。除此之外，它们还使用HSM来实现工业级安全性。通过使用HSM，它们可以确保在无需任何单个节点故障的情况下仍然安全。



### dBFT

毫无争议的事实是PoW和PoS是广为人知的共识算法。虽然很多区块链生态系统使用这两种通用的算法，但有些试图强加更新、更高级的共识系统。在这些先锋区块链品牌中，NEO的名字肯定会出现。

随着过去一年的蓬勃发展中，NEO现在已成为业界的热门蛋糕。中国品牌展现出了相当的潜力。但为什么是他们呢？因为他们是先进共识定理的发明者--委托拜占庭容错dBFT。


#### NEO：受欢迎的区块链技术

NEO是现在市场上最受欢迎的加密货币之一。某段时间内它被认为是中国的“以太坊”。该网络的主要焦点是创建智能经济，你可以以低价共享你的数字资产。

NEO使用dBFT来验证所有的交易。如果你在你的NEO中参与赌注，你将能生成GAS。GAS是该平台的主要流通货币。你将必须为每笔交易支付一定量的GAS费用。这是为什么你有囤有越多的NEO，你将会获得更多的GAS。

但是，这种赌注和PoS相比略有不同。

许多交易所提供一个交易池系统。但是，最好的方式是使用NEO官方的钱包而不是其他的存储钱包。

在我们分析dBFT之前，我们必须让你知道该算法之父遗留下来的一些问题--拜占庭容错共识算法。


#### 拜占庭将军问题的缺点！

当我们目睹任何善意投票及其结果时，系统的一个主要缺点就会出现。但是是怎样的方式呢？为了更好的理解这个缺点，你需要掌握一个算法示例。

你已经知道遵循dBFT一致性算法的节点称为军队。一支节点的军队只有一个将军，并且这些节点总是听从将军的指令。

现在想象一下，拜占庭军队打算攻打罗马并将它拿下。让我们仔细考虑下拜占庭军队的9位将军和将军围攻城市并准备进攻！他们可以攻下罗马，只要将军们听从统一的、单一的策略进行攻击或者撤退。

现在我们明白了。将军们有着独特的性质--他们将遵循51%的投票结果。但这里有另一个扭曲的结果。将军们不会坐在圆桌上讨论决定。相反，他们在不同的位置上互相传递消息。


#### 四个威胁！

这里有四个可能的方式可以帮助罗马人保留王位。

第一，罗马人可以试图贿赂将军们并获得他们的青睐。那些接受贿赂的将军会被认为是“叛国将军”。

第二，任何一个将军都会做出错误的决定来对抗集体的意愿。这些将军将被认为是“无法正常运作的将军”。

第三，信使或者快递员可以被罗马人贿赂并传送误导性的决定给其他将军。

最后，第四点，罗马人可以杀死快递员或者信使来破坏将军们的通信网络。

所以，拜占庭容错有四个重要的错误使得该共识算法不完美。


#### dBFT是如何改变场景的？

不要着急，NEO向我们展示了解决拜占庭将军问题的更好方法。现在让我们看看NEO引以为傲的委托拜占庭容错共识机制。dBFT主要侧重于以两种方式来解决已有模型--更好的可拓展性和更好的性能。


#### 发言人和代表们！

我们将再次使用另一个例子来搞清楚dBFT模型。让我们考虑下拜占庭军队有一位当选的领导人而不是一位官僚将军。这位被选中的领导人将担任军队的代表。

你可以想到将军们民主地被这些当选的代表所取代。甚至军队也不同意这些代表或者选举另一个新的代表来取代先前的代表。

该举措限制了将军们的权利，没有将军可以背叛整个军队。所以，罗马人现在不能只是贿赂和买通将军来为他们工作了。

在dBFT中，当选代表必须跟踪各个节点的决策。分散的分类账本记录了所有节点的决策。

节点所在的军队也选举一位发言人来与代表们分享它们共同的、统一的想法。为了通过新的法案，发言人向代表们分享军队中节点们的意见，至少要有66%的代表就议案达成一致。否则，提议失败。

如果该议案没有得到66%的代表们的批准，提议将被拒绝，而新的议案继续会被提议直到达到共识为止。这个过程保护整个军队免受叛徒或者背叛将军们的影响。


#### 不诚实的发言人们

这里仍然有两个可能的场景会阻碍dBFT区块链共识算法的完整性--不诚实的发言人和不诚实的代表。

dBFT区块链共识协议也为我们提供了解决这些场景的方法。正如我们所说，账本将节点的决策保存在某个地方。代表们会验证发言人所描述的是否属实。如果发言人的提议和账本无法关联，66%的代表会拒绝发言人的提议并且完全禁止该发言人。


#### 不诚实的代表们

另一个场景是有一个诚实的发言人，但可能背叛了代表。这里，诚实的代表和诚实的发言人将努力成为66%的大多数，并降低不诚实的代表的努力。

那么，你可以看到dBFT是如何克服拜占庭将军的缺陷和BFT共识算法。诚然，NEO值得世界各地的赞扬，他们努力创造了一个更好的共识算法。



### DAG(Directed Acyclic Graphs)

许多加密专家认为比特币是区块链的1.0版本，而以太坊是区块链的2.0版本。但是现在，我们可以看到市场上的新玩家拥有更加现代化的技术。

有些人还说这是区块链3.0。虽然许多竞争者都在争取区块链3.0的称号，但NXT将通过有向非循环图(也称为DAG)的应用领先于游戏行业。抛开NXT不说，IOTA和IoT链也在它们的系统中使用了DAG。


#### DAG是如何工作的？

你可以认为DAG是一个共识算法。但是DAG是基于数据结构的一种形式。虽然大多数区块链是包含数据块、链，但DAG是一个无缝图，其数据以拓扑形式存储。DAG可以方便的处理类似数据处理、路由和压缩这样的特定问题。

在PoW共识算法中生成一个块需要10分钟的时间。是的，PoW慢透了。DAG不是在单一链上工作的，而是实现了侧链。侧链允许不同的交易在多个链上独立地执行。

这将减少创建和验证区块的时间。好吧，实际上它完全消除了块的必要性。而且，挖矿似乎也浪费时间和精力。

这里，所有的交易都是有向的并且保持特定的序列。而且，系统是非循环的，这意味着找到父节点的机会为0，因为它是节点树，而不是节点循环。DAG向全世界展示了区块链没有区块的可能性。


#### DAG的基本概念

* 没有双重支付

传统的区块链允许在特定时间进行单个区块的开采。有可能有多个矿工会试图验证同一个区块。这可产生双重支付的可能性。

而且，该情况可能导致软件硬分叉。DAG根据先前的交易数量来验证特定的交易。这使得区块链系统更安全、更健壮。

* 减少宽度

在其他区块链共识算法中，节点得到的交易会添加到整个网络。这会使得系统宽度读更庞大。而且，DAG将新的交易链接到旧的交易图上。这使得整个网络更加精简，更直接地验证特定交易。

* 更快更聪明

正如DAG的无区块特性，它可以更快的处理交易。事实上，它使得PoW和PoS在比赛中看起来像老爷爷一样慢。

* 有利于较小的交易

并不是所有人都在交易中交易数百万美元。事实上，小额的支付更常见。但是比特币和以太坊的大笔支付费用对小额交易不太友好，在另一方面，DAG非常适合较小的交易，因为可以忽略交易费用。




## 第七章：其他类型的共识算法

### Proof of Activity

当人们在讨论PoW和PoS的话题时，莱特币的创始人和其他三位作者想到了一些非常棒的事情。他们向世界提出了一个简单的问题--为什么不能把PoW和PoS结合起来而是让它们相互争斗呢？

因此，一个迷人的混合观点便面向于世--PoA活动证明。它结合了两种共识算法最好的特点--更安全的抵御任何攻击，而不是一个不耗电的系统。


#### PoA是如何工作的？

在PoA区块链共识算法协议中，挖矿过程的开始就像PoW算法一样。矿工解决一个关键谜题来获得报酬。那么，它与PoW关键区别在哪里呢？在PoW中，矿工开采有完整的交易的区块。

在PoA中，矿工只挖掘区块的模版。这样的一个模版中有两件事情需要矿工去做--头信息和矿工的奖励地址。

有一次，矿工挖掘这些区块的模版。系统会转换为PoS。在区块中的头信息指向一个随机的股东。这些股东之后验证预先开采的区块。

验证者持有的堆栈越多，它们批准块的可能性就会越大。只有在验证后，该特定块会被加入到区块链中。

这就是PoA，如何使用两种共识算法的最佳算法来验证区块并将其添加到区块链中。此外，网络也会付给矿工和验证者平等的份额作为交易费用。因此，该系统抵抗“共同的悲剧“，并为区块验证创建了更好的解决方案。


#### PoA的影响

区块链面对的最大的威胁之一是51%算力攻击。共识定理将51%攻击的可能性降低到0。它发生的原因是矿工和验证者都不能占多数。因为在向网络中添加块时，该过程需要同等的贡献。

尽管这样，一些批评家认为，PoA区块链共识协议有一些严重缺陷。第一个便是由采矿特性导致的大量能源消耗。第二，PoA没有任何解决方案来阻止验证者的双重签名问题。这两个重大的缺陷使得该共识定理有点落后。

两个受欢迎的区块链平台采用PoA--Decred和Espers。但是，它们还有些变化。实际上，Decred被认为是比Espers共识定理更受欢迎的。



### Proof of Importance

接下来在我们列表中出现的是重要性证明区块链共识协议。该共识案例的由来是因为NEM的名字而闻名。该概念是在PoS的基础上发展而来的。尽管如此，但NEM引入了一些新的想法--收获或者保留退休金的权利。

收获机制决定一个节点是否有资格被添加到区块链中。你在一个节点上收获的越多，则它有更多的机会被添加到链中。作为收获的回报，节点接收验证者收集的交易费用作为奖励。要获得收获资格，你的账户上至少要有10000个XEM。

该机制解决了PoS的主要问题。在PoS中，与那些拥有少量金币的验证者相比，富有的人拥有更多金币。例如，如果你拥有20%的加密货币，择你可以在区块链网络上挖掘20%的区块。这就导致了该共识算法更青睐有钱的人。


#### 显著的重要性证明特征

* 保留退休金的权利

该共识定理中最有趣特性是保留退休金的权利或者收获。正如我们所说的那样，你至少需要10000个金币才有资格在开始的时候进行收获。你的PoI得分依赖于你拥有的收获金额。但是，该共识算法考虑了你口袋中硬币的有效期限。

* 交易合作伙伴

如果你与其他NEM账户持有者进行交易的话，那么PoI算法将会奖励你。该网络会将你视为合作伙伴。如果打算伪装这种伙伴关，系统可以发现你。

* 评分系统

交易会对你的PoI分数产生影响。分数是基于你在30天内完成的交易。更频繁和更本质的总和将会帮助你在NEM网络中提升你的分数。



### Proof of Capacity

容量证明共识示例是著名的PoW共识协议的升级版本。该协议本质的特点之一是计谋。在开始挖矿之前你将必须贡献你的计算机算力和硬盘存储。

该系统比PoW更快也是在自然之中。PoC仅仅用4分钟就可以创建一个区块，而PoW却要10分钟。而且，该系统试图解决PoW系统中的哈希问题。你的电脑上有越多的解决办法和计谋时，你将有更好的机会来赢得挖矿对决。


#### 容量证明机制是如何工作的？

为了理解该共识定理的本质，你必须要了解两个概念--计谋和挖矿。

通过合理安排你电脑的硬盘，你基本上可以创建一个随机数。该随机数和比特币中的随机数还有些不同。这里，你将必须计算出你的ID和数据的哈希值直到你算出这个随机数。

每个随机数捆绑着8192个哈希值。捆绑哈希值又称为挖矿。每个ID可以接收的最大的范围是4095个。

下一个概念是在硬盘上挖矿。正如我们所说，你可以在同一时间收到0-4095个范围内的金币并且存储在你的硬盘上。你将被分配一个最低截止日期来解决随机数。这个期限也表明了创建块的时间。

如果你比其他矿工更早地解决这些问题，你将会得到一个块作为奖励。一个著名的例子便是Burst也采用了PoC算法。


#### 容量证明的利和弊

在硬盘上挖矿比常规的PoW更为节能。你将不必花费多少钱来获得我们在比特币协议中看到的昂贵的采矿设备。在该共识算法上，家用PC的硬盘就可以满足挖矿。

讲真，该区块链共识算法也有很严重的问题。首先，该过程会在硬盘上创建大量的冗余数据。该系统青睐于那些拥有足够大的存储单元能对去中心化概念提出一个威胁的矿工。甚至黑客也可以利用该系统或者注入恶意挖矿软件到系统中。



### Proof of Burn

该共识序列是相当令人印象深刻的。为了安全保护PoW加密货币，一部分金币将会被烧掉。当矿工将金币转账给食用者地址时，该过程便会发生。该食用地址无法用于任何目的。账本记录这些燃烧掉的金币，使得它们完全不可以继续花费。烧掉金币的用户可以得到一份奖励。

是的，燃烧意味着失去。但是该过程在长久防护金币免受黑客的网络攻击中来说，其损害是暂时的。而且，燃烧过程增加了可选择金币的赌注。

在该场景下可以增加用户在下一个区块挖矿的机会，也增加了他们在未来的奖励。因此，燃烧可以被用于挖矿优先级中。在加密货币中相应的部分是一个非常好的共识案例，可以使用该区块共识算法。


#### 食用者地址

为了烧掉金币，用户会将金币发送到食用者地址。食用者地址并没有任何私钥。因此，没有用户可以访问这些地址来消费这些金币。而且，这些地址以随机方式生成。

尽管这些金币不可访问或者永远消失了，但是它们被视为计算供应并标记为烧毁。


#### 燃烧证明的利与弊

燃烧金币背后的主要原因是为了创造更好的稳定性。我们知道长期玩家往往长期持有金币以此来获利。

该系统通过提供更稳定的货币和长期承诺来支持这些长期的投资者。此外，这增强了去中心化并创建了更好的分布式网络。

但是无论你从那个角度来看该场景，燃烧金币就意味着浪费了它。甚至一些食用者地址在这里面也拥有超过100000美元价值的比特币。这里没有方法可以恢复这些金币，它们只能被烧掉。



### Proof of Weight

好的，PoWeight区块链共识协议是我们列表上的最后一个共识算法了。它是PoS的重大升级版本。在PoS中，你拥有的令牌越多，你就有更多的机会来发现更多的区块。该些想法使得系统有很大的偏见。

好吧，PoWeight试图解决PoS中这种偏见。像Algorand，Filecoin和Chia这样的加密货币都实现了PoWeight。PoWeight考虑了一些其他因素，而不是像PoS中那样拥有更多的令牌。

这些因素被认为是加权因子。例如，Filecoin会考虑你拥有的IPFS数据量并权衡该因子。其他一些因素包括但不限于PoSpacetime和PoReputation共识协议。

该系统的基础优势包括可定制和可拓展性。尽管对该共识算法来说激励是一个很大的挑战。



#### **各个共识算法之间的比较**


| 共识算法 | 区块链平台 | 起始时间 | 编程语言 | 智能合约 | 优点 | 缺点 |
| --- | --- | --- | --- | --- | --- | --- |
| PoW | Bitcoin | 2009 | C++ | 否 | 受51%攻击的机会更少；更好的安全性 | 巨大的能量消耗；中心化的矿工 |
| PoS | NXT | 2013 | Java | 是 | 能效；去中心化 | 没有任何危险的问题 |
| DPoS | Lisk | 2016 | JS | 否 | 高效节能；可拓展；安全性增加 | 部分中心化；双花攻击 |
| LPoS | Waves | 2016 | Scala | 是 | 使用轻便；租赁金币 | 去中心化问题 |
| PoET | Hyberledger Sawtooth | 2018 | Python/JS/Go/C++/Java/Rust | 是 | 廉价参与 | 需要特定的硬件；对公链不友好 |
| PBFT | Hyperledger Fabric | 2015 | JS/Python/Java/REST/Go | 是 | 无需确认；能源减少 | 沟通鸿沟；女巫攻击 |
| SBFT | Chain | 2014 | Java/Node/Ruby | 否 | 良好的安全性；签名验证 | 无法在公链使用 |
| DBFT | NEO | 2016 | Python/.NET/Java/C++/C/Go/Kotlin/JS | 是 | 可拓展；快速 | 在链中有冲突产生 |
| DAG | IOTA | 2015 | JS/Rust/Java/Go/C++ | 确认中 | 低成本网络；可拓展性 | 实现鸿沟；不适合只能合约 |
| PoA | Decred | 2016 | Go | 是 | 减少了51%攻击的可能性；平等贡献 | 巨大能量消耗；双签名 |
| PoI | NEM | 2015 | Java/G++XEM | 是 | 保留退休金权利；交易关系 | 去中心化问题 |
| PoC | Burstcoin | 2014 | Java | 是 | 廉价；效率；分布式 | 喜欢更大的利益；区中心化问题 |
| PoB | Slimcoin | 2014 | Python/C++/Shell/JS | 否 | 网络保留 | 不适合短期投资；浪费金币|
| PoWeight | Filecoin | 2017 | SNARK/STARK | 是 | 可拓展；可定制 | 激励问题 |


## 第八章：结论

正是共识算法使得区块链网络的本质变得如此通用。是的，没有一个共识算法可以被区块链称之为完美的。但这就是我们猜测的技术之美--不断变化的改善。

如果这些共识算法没有出现，我们可能仍然依赖着PoW共识机制，无论你是否喜欢，PoW都会威胁到区块链的去中心化和分布性。

区块链技术的整个想法便是为了去中心化和对抗专制，现在正是该普通人制止腐败和错误系统的时候了。

我们迫不及待地等待更好的共识算法，这些算法将改变我们的生活，共创美好的明天。








