initialize() {
	initializeSLiMModelType("nonWF");
	defineConstant("L", 3e9);
	defineConstant("K", 600);
	defineConstant("PiI", 0.05);
	defineConstant("PiMax", 0.2);
	defineConstant("AiI", 0.001);
	defineConstant("AiMax", 0.1);
	defineConstant("Pi_dr", 1e-5);
	defineConstant("GRPi", 0.0003);
	defineConstant("GRAi", 0.0001);
	defineConstant("MaxAge", 50);
	initializeMutationType("m1", 0.5, "f", 0.01);
	initializeMutationType("m2", 0.5, "f", 0.1);
	initializeMutationType("m3", 0.5, "f", 0);
	initializeMutationType("m4", 1, "f", -10);
	initializeGenomicElementType("g1", c(m1, m2,m3), c(0.8,1e-3,0.0));
	initializeGenomicElement(g1, 0, L-1);
	initializeMutationRate(2e-10);
	initializeRecombinationRate(0);
}

reproduction() {
	mutcounts = individual.genome1.countOfMutationsOfType(m2);
	if (mutcounts >= 10){
		nonimmortal = 0;
	}
	else
	{
		nonimmortal = 1;
	}
	 
	p_death = AiMax/((1+(AiMax-AiI)/AiI)*exp(-GRAi*mutcounts)) + nonimmortal*(1/MaxAge);

	draw = runif(1);
	if (p_death >= draw){
			individual.genome1.addNewDrawnMutation(m4, 1);
	}
	else 
	{
		p_prol = PiI * (1-Pi_dr)^p1.individualCount+PiMax/((1+(PiMax-1e-9)/1e-9)*exp(-GRPi*mutcounts));
		if (p_prol >= draw){
			o1 = subpop.addCloned(individual);
			o1.age = individual.age + 1;
			o2 = subpop.addCloned(individual);
			o2.age = individual.age +1;
			individual.genome1.addNewDrawnMutation(m4, 1);
		}
		else
		{
			individual.age = individual.age - 1;
		}
	}
}


1 early() {
	sim.addSubpop("p1", 100);
	log = sim.createLogFile("~/sim_log.txt", logInterval=10);
	log.addGeneration();
	log.addPopulationSize();
}


1000 late() { 
sim.outputFixedMutations(); }
