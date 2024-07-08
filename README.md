# Predictive methods for gearbox health assessment

The work mainly concentrates on building a machine learning model using the available master motor load and slave motor load data to predict the failure of gearbox.
A Graphical user interface is built for the communication of human with the machine learning model.
The project is then deployed into cloud (We used AWS as platform in this project) so that anyone with any device connected to the internet can access the condition of gearbox.

Work Breakdown Structure for the project:-

1.Dataset Collection

2.Preprocessing of data

3.Generation of Synthetic data for breakdown

4.Model development

5.Develop a Flask app.

6.Deployment of app on Cloud ( We used AWS here )

Advantages:-

Real time continuous monitoring of the gearbox can be done by using this approach. Which reduces the requirement of checking the gearbox for every time interval. Everything can be monitored from the mobile.
Breakdown warnings can be instantiated using this approach which predicts the breakdown that’s going to happen in future.
As everything is running on cloud server there is no need of buying any external computer and making any physical setup. Only a rent of around Rs.8500/- can provide monitoring for 365 days 24/7.

Conclusion:-
This project successfully demonstrated the application of machine learning to predict gearbox failures in DRI-I plant, focusing on analyzing the master and slave motor load readings from the kiln. By leveraging historical load data and advanced machine learning techniques, a robust predictive model was developed and deployed on AWS, providing real-time failure predictions.
The advantages of this project include enhanced operational efficiency, cost savings, extended equipment lifespan, and data-driven decision-making capabilities. The scalable, real-time monitoring solution ensures the plant can maintain high performance while adapting to changing operational conditions. Overall, this project highlights the transformative potential of predictive maintenance in industrial settings, emphasizing the importance of data analytics and machine learning in optimizing maintenance operations and ensuring continuous, efficient plant operations.

