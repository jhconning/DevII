---
marp: true
---

 <!-- page_number: true -->
# Development II 

## Spring 2020



Jonathan Conning

**Hunter College and The Graduate Center*** 

**City University of New York**

---

# Week 1

- Class materials: https://dev-ii-seminar.readthedocs.io/
  - syllabus, reading list
  - notebooks, slides, etc.

---

## Grading

- 35% Presentations and Participations
- 35% Midterm and Assignments
- 30% Final Project 

All are expected to read articles carefully and participate in discussion. 
Each week two students are topic 'leaders.'.  Before class distribute critical paper summary and list of questions for class. 

Topics set partly by me, partly by your suggestions 

---

## Introductions 



---

### Economic history periodization and schools of thought

(de Janvry and Sadoulet, 2016)

---

## Why isn't the whole world developed?

- Technology and other assumptions
- Neo-classical benchmarks
  - Efficient allocation and convergence
    - Solow Growth 
    - Trade 
    - Factor movement
- Misallocation
  - Lewis, dualism and its critics
  - enduring puzzles
  - modern takes

---

Lucas, Robert E. 1990. “Why Doesn’t Capital Flow from Rich to Poor Countries?” *American Economic Review* 80 (2): 92–96. [link](https://docs.google.com/viewer?url=https%3A%2F%2Fwww.econ.nyu.edu%2Fuser%2Fdebraj%2FCourses%2FReadings%2FLucasParadox.pdf)  

Gollin, Douglas. 2014. “The Lewis Model: A 60-Year Retrospective.” *Journal of Economic Perspectives* 28 (3): 71–88. [link](https://sites.google.com/site/douglasgollin/doug-gollin/research)

Gollin, Douglas, David Lagakos, and Michael E. Waugh. 2013. “The Agricultural Productivity Gap.” *The Quarterly Journal of Economics* 129 (2): 939–993. ([link](https://sites.google.com/site/douglasgollin/doug-gollin/research))

Also useful: [jupyter notebooks](http://dev-ii-seminar.readthedocs.io/en/latest/index.html) on Specific Factors, Edgeworth Boxes and Lucas 1990.

---
# Week 2  (2/4)
 ####  Puzzles and Neoclassical and Institutional Frames
* Lucas, Robert E. "Why Doesn't Capital Flow from Rich to Poor Countries?" The American Economic Review (1990): 92-96.

* Gollin, Douglas, David Lagakos, and Michael E. Waugh. 2013. “The Agricultural Productivity Gap.” The Quarterly Journal of Economics 129 (2): 939–993.   

---

### Theories of institutions and institutional change

* North, Douglass. 1990. “An Introduction..,” chapter 1 in Institutions, Institutional Change, and Economic Performance. Cambridge ; New York: Cambridge University Press.  

* (o) Bardhan, Pranab. 1989. “Alternative Approaches to the Theory of Institutions in Economic Development.” chapter 1 in The Economic Theory of Agrarian Institutions. Oxford University Press  

* (o) Acemoglu, Daron, Simon Johnson, and James A. Robinson. 2005. “Institutions as a Fundamental Cause of Long-Run Growth.” Handbook of Economic Growth 1: 385–472. (selections)

---
### Next week (Empirical institutions)
  
* Dell, Melissa. "The Persistent Effects of Peru's Mining Mita." Econometrica 78, no. 6 (2010): 1863-903.[link to paper] [to data and code for replication]

* Nunn, Nathan. 2008. “The Long-Term Effects of Africa’s Slave Trades.” The Quarterly Journal of Economics 123 (1): 139–176.[link to paper and data and code for replication]

contd.

---
(to further study RDD, interesting, replicable papers)
* Meyersson, Erik. 2014. “Islamic Rule and the Empowerment of the Poor and Pious.” Econometrica 82 (1): 229–269.
  
* Bubb, Ryan. 2013. “The Evolution of Property Rights: State Law or Informal Norms?” The Journal of Law & Economics 56 (3): 555–94. 


Week that follows: modeling Property Rights, Conflict, and Equilibrium agrarian structures.

---
## Neoclassical Models
- Assumptions, Tricks and main Predictions
  


---
## Homogeneous and Homothetic Production Functions

A function is homogenous of degree $k$ if:

$$F(\tau K,\tau L)=\tau^k F(K,L)$$

Linear-homogeneous or Constant Returns to Scale (k=1): 
$$F(\tau K,\tau L)=\tau F(K,L)$$

Fix any one factor, diminishing returns to the 

---

## Production in intensive form (output per worker).

 If k=1, set $\tau =\frac{1}{L}$ :  $F(\frac{K}{L},1) = \frac{F(K,L)}{L}=f(k)$

where $k=\frac{K}{L}$, capital per worker. $f'(k)>0, f''(k) \le 0$

---
## Homogenous $\rightarrow$ Homothetic 

If $F$ is homog. of degree $k$, marginal products are homog. of degree $k-1$.  

Take derivative of each side of $F(\tau K,\tau L)=\tau^k F(K,L)$ wrt to $K$ and $L$ respectively:

$$F_K(\tau K, \tau L)=\tau^{k-1}F_K(K,L)$$

$$F_L(\tau K,\tau L)=\tau^{k-1}F_L(K,L)$$

Implies that the rate of technical substitution (RTS) or the slope of any isoquant along any ray from the origin is the same:

$$\frac{F_L(\tau K, \tau L)}{F_K(\tau K, \tau L)}=\frac{F_L(K,L)}{F_K(K,L)}$$

---
The Rate of technical substitution (RTS) or slope of any isoquant along any ray from the origin is the same:
![](media/homog.png)

A strong assumption with convenient simplifying implications

---
## Euler's Theorem

Recall 
$$F(\tau K,\tau L)=\tau^k F(K,L)$$

Take derivative wrt to $\tau$

$$k \cdot \tau^{k-1} F(K,L)=F_K \cdot K + F_L \cdot L$$

When $k=1$ (CRS)

$$F(K,L)=F_K \cdot K + F_L \cdot L$$

---
## CRS + competition $\rightarrow$ zero economic profits

On competitive markets $r=p \cdot F_K$  and $w=p \cdot F_L$ so we get

$$F(K,L)=F_K \cdot K + F_L \cdot L$$

$$p \cdot F(K,L)=p \cdot F_K \cdot K + p \cdot F_L \cdot L$$

$$p \cdot F(K,L)=r \cdot K + w \cdot L$$

Factor payments exhaust total product

---
Factor payments exhaust total product
$$p \cdot F(K,L)=r \cdot K + w \cdot L$$

So firm profits must be zero
$$
\Pi(K,L) = p \cdot F(K,L) - w \cdot L - r \cdot K =0
$$ 

- $K$ and $L$ only factors used in production, any residual rents competed away.
- Later we'll add 'skill/entrepreneurship' as non-traded factor
   - firm profit then interpreted as return to non-traded factor(s)  

---

Profit Maximization: 
 $$p \cdot F_L(K,L) = w$$
 $$p \cdot F_K(K,L) = r$$


---

![](media/ldemand.png)

---

In intensive form: 


- $r=f'(k)$  

- $w=f(k) - f'(k) \cdot k$   

   - wage = output per worker hour minus payments to capital per worker hour equal wage per worker hour.


---
With Constant Returns to Scale ($k=1$)

$F_L(\tau K, \tau L)=F_L(K,L)$ 
$F_K(\tau K, \tau L)=F_K(K,L)$

In a competitive market firms marginal factor hiring will equalize factor prices.

$F_L(\tau K, \tau L)=w=F_L(K,L)$ 

Can determine $\frac{K}{L}$ ratio but not scale of $K$ and $L$ on each firm. 
Any two firms with same have the same $\frac{K}{L}$ have same marginal products $F_K$ and $F_L$.  

---
### Firm scale indeterminate 
- CRS $\rightarrow$ the size distribution of firms is *indeterminate*

- Firms could be all same size, some large and other small, etc.  We can't tell, nor does it really matter. 

- Another way to see: under CRS, MC(Q) and AC(Q) cost are same (horizontal) across firms. So cannot determine firm's optimal scale from $P=MC(Q)$.

- Each firm is a blown up or scaled down version of the next. We can treat sectororal output as if produced by a single competitive firm.

---
#### What if we shutdown one market?

- Suppose each firm $F(K_i,L_i)$ is homog of degree 1.  Can we still achieve efficient resource allocation despite a total shutdown of capital market?

With CRS technology yes:

- Efficiency requires equalizing capital-labor ratio $\frac{K_i}{L_i}=\frac{K_j}{L_j}$
- So if firms $i,j$ have fixed capital $\bar K_i$ $\bar K_j$ we can get efficient allocation by just adjusting labor use across firms until:

$$
L_i =  L_j \cdot \frac{\bar K_i}{\bar K_j} 
$$

---

## Cobb-Douglass production 

$$F(K,L) = A \cdot K^\alpha L^\beta$$

- $A$ interpreted as total factor productivity parameter

- Degree of homogeneity $k=\alpha +\beta$

---

If $k=1$ then $\beta=1-\alpha$, then  $F_L =  (1-\alpha) A \cdot \frac{K^\alpha L^{1-\alpha}}{L}$

Marginal products are a constant proportion of average products

$$F_L= (1-\alpha) \cdot \frac{  F(K,L)}{L}$$

and 

$$F_K= \alpha \cdot  \frac{F(K,L)}{L}$$

---

# Two sector Specific Factors Model

Variations of the model (see [jupyter notebook](http://dev-ii-seminar.readthedocs.io/en/latest/notebooks/SFM.html))

- Two-sector model (short-run version of Hecksher-Ohlin-Samuelson) 
- Workhorse model:
  - Income distribution and Political economy
  - Migration across countries, sectors
  - dualism, Lewis, Harris Todaro
  - (mis)allocation across and within sectors.

---

## Aggregate Production Function Models

### What are 'Egalitarian predictions' of neo-classical model (Lucas, 1990)?

---
### Neo-classical Convergence

- CRS $\rightarrow$ diminishing returns to any one factor when others held fixed.
   - implies $r=f'(k)$ falls as $k=\frac{K}{L}$ increases
   - (with same technology) 'poorer' countries have lower $k$ but higher $r$, lower $w$
- Convergence mechanisms
  - Capital or Labor Movement model
  - Solow/Neo-classical Growth model 
  - Hecksher-Ohlin-Samuelson (two sector) Trade models

---

With same technology:
  - differences in output per person due to differences in $\frac{K}{L}$ 
  - Lower $\frac{K}{L}$ countries have higher $r$ and lower $w$
  - Market forces (capital and labor movement in search of higher returns, higher return to savings, trade in goods) all push toward factor price equalization and income convergence. 
  

---

## Solow Growth Model

$y=k^\alpha$

$\frac{dk}{dt} = s \cdot k^\alpha - (n+g+\delta) k$

Steady state:  

$$k^* = \left( \frac{s}{n+g+\delta}  \right )^\frac{1}{1-\alpha}$$

Convergence regardless of starting point.

Countries further away from steady state grow faster (catch up or converge)

---

## Capital mobility

Diminishing marginal product of capital implies that countries that if there are two countries with the same production technology 

- country with less accumulated capital per worker has higher $r=f'(k)$
- capital should flow from rich to poor countries, accelerating convergence.

See Lucas (1990) [jupyter notebook](http://dev-ii-seminar.readthedocs.io/en/latest/notebooks/Lucas90.html)

---

## Institutions as Fundamental 


## 


---
# USA experience
![](media/ronUS.png)


source: Ron (2021) [Origins of the US Agricultural State](https://broadstreet.blog/2021/09/03/slavery-technology-and-the-social-origins-of-the-us-agricultural-state/)

---
![bg center:50%](media/USfreefarms.png)

---

# USA: squatter nation

- Claims clubs and frontier policy driven from below.
- Adverse possession and premption laws. Later free or low price land via Homestead Acts.
- "a vast agricultural reform movement that arose between the American Revolution and the Civil War to demand novel federal policies that were fiercely opposed by slaveholders. (Ron, 2020)"

Soto, Hernando de. 2001. “Citadels of Dead Capital: What the Third World Must Learn from U.S. History.” *Reason* May. [link](http://reason.com/0105/fe.hs.citadels.sht)

Murtazashvili, Ilia. 2013. *The Political Economy of the American Frontier*. Cambridge University Press.

---