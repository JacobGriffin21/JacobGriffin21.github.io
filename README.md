###### JacobGriffin21.github.io

# CS499 ePortfolio

### Introduction/Professional Assesment
Hello, My name is Jacob Griffin and I have been in the Computer Sceince program at SNHU for 2 years. Throughout this Capstone course, it has showed me the strides I have made in the CS career field, as well as my concentration in Software Engineering. When reviewing this github pages you see will various artifacts that I have enhanced and now meet professional standards. There are software programs showcased on this page that have been converted to cloud databases from local databases that had no chance in becoming scalable and offering a professional source to an organizaiton until the enhancement was made, and you will also see legacy code that was completely overridden and transformed into a more robust and effecient programming language that not only benefited the consumers, but the future developers and maintainers of the software.

Throughout this course and previous courses, I have not only improved as a programmer, but I have adopted the ability to communicate effectively with other team members, stakeholders, etc. I am able to fully and completely understand what the consumer is wanting/needing and values in the product they are investing in. With that, I can brief stakeholders on progress of their appilcation, future updates, areas that need improvement, etc, but I have the skills to do this effectively with not just stakeholders, but as well as team leads, other development teams, which aids in a colloborative and cohesive workplace. Following this introduction you will see an overview of my 3 artifacts with 3 enhancements that include the following, Artifact 1 is from my CS 340 course where I added Unit Testing for a CRUD module that stored dogs from an animal shelter, the 2nd Artifact is from my CS 300 course where I implemented a 'lazy deletion' method inside a Binary Search Tree, and the 3rd Artifact is also from the CS340 course where I converted a local MONGODB database into a MONGODB Atlas cloud server. 

### Code Review:
Link:<br>
[https://youtu.be/P7IM1piKQ7Q](https://youtu.be/P7IM1piKQ7Q)<br><br><br>


### Enhancement 1:
Link to Original Code: 
[https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Artifact%201%20original%20Code](https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Artifact%201%20original%20Code)

Link to Enhanced Code: [https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Enhancement%20One](https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Enhancement%20One)

The first artifact comes from my CS 340 class and satisfies the Software Engineering and Design category. For this artifact we created a program for an Animal Shelter that housed dogs. The program provided a dashboard to users where they could filter by the type of rescue dog they were searching for. Within the dashboard there was also a geo map that allowed the consumer to be able to see the location of all the dogs within the animal shelter. Users had the ability to create, read, update, or delete animals, this is where the program used the CRUD method. The original software had no type of testing to ensure that the four methods were functioning correctly. This is where the enhancement I implemented comes into play. 

I created four unitTest with the Python built in library that verified that all four methods were working as intended. I utilized 'dummy' data and the local MONGODB database within Mongo Compass to verify that these methods functioned correctly. When data was created, the unitTest would provide a print statement that the data was successfully created, and the built in library would return the value that ensured all test passed. After testing each method, I would check within Mongo Compass to ensure that the enhancement was a success. 
My enhancemnet allowed me to showcase skills in mnay areas such as test cases, identifying all the testable componenets within code, ensure functionality before deployment, and provide an improvement that will be beneifical both to the users and the future developers. This enhancement also satisfied the course outcomes of design, develop, and deliver professional-quality oral, written, and visual communication that are coherent, technically sound and appropriately adapted to specific audiences and contexts. This outcome is satisfied because my code is well documented, it is professional quality, and is specific to the audience of software developers that will benefit from this implementation. I also satisfied the course outcome that demonstrates an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliveer value and accomplish indsutry specific goals. Not only does my enhancement satisfy the previous course outcomes, it satisfies that outcome that i have developed a security mindset as unitTesting ensures proper functionality and leaves no vulnerabtilty for threats. 

### Overview of Changes for Enhancement One
- CRUD unitTesting implementation with Python built in Library to ensure correct functionality<br><br><br>


### Enhancement 2:
Link to Original Code: 
[https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Artifact%202%20Original%20Code](https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Artifact%202%20Original%20Code)

Link to Enhanced Code: [https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Enhancement%20Two](https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Enhancement%20Two)

The second artifact comes from my CS 300 class and satisfies the Algorithms and Data Structures category. For this artifact, we created a program for a local auction that would store bids from consumers and output the winning bid utilizing a binary search stree data structure (BST). With this program, users would input their bid, and the program utilized a while loop to continue running until there were no more bids, and the boolean value flipped, causing the software to exit, and output the highest bidder. The original code used a BST to add, delete, and find bids. For this program it had a longer run time due to the restructuring of the BST when nodes were deleted.

For my enhancement I implemented what is called a 'lazy deletion' method which does not require the restructuring of the tree when a node is deleted. The lazy deletion uses an algorithm where when a user deletes a bid, it flags the bid as deleted but it doesn't actually remove the node. Instead of removing the node, it marks the node as deleted, and it is no longer able to be found when searching for the bid, and the BST maintains its balanced structure, decreasing run time, and providing a more enhanced program for the users. The second enhancement I made for this program is converting it to Python from C++. Since C++ does not utilize autmatic memory management, and Python does, due to the program needing to hold a large set of data, Python makes the best implementation as it will automatically manage the memory and reduce the complexity of the code. With implementing Python, it made the code less complex, more readable, and easier to maintain for future developers. 
The course outcomes that are met with these two enhancements are employing strategies for building collaborative environments that enable diverse audiences to support organizational decision-making in the field of computer science. I met this course outcome by providing well documented code, providing less complex code and enabling to a diverse audience, resulting in collobartive opportunities. The improvemenmt also met two other course outcomes, which are design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices, and demonstrating an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals. I satisified both of these outcomes by evaluating the current computing solution and implementing a solution that would enhannce the user experience by utililzing algorithmic principles such as a BST with a 'lazy deletion' method, and I demonstrated by abilities to use well-founded innvoation techniques such as improving the run time by a new technique that is becoming widely popular amongst developers that use BST. 

### Overview of Changes for Enhancement Two
- Implemented 'Lazy Deletion' method to decrease runtime and maintain the BST integrity when bids are deleted
- Converted the legacy code to Pyton<br><br><br>


### Enhancement 3:
Link to Original Code: 
[https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Artifact%203%20Original%20Code](https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Artifact%203%20Original%20Code)

Link to Enhanced Code: [https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Enhancement%20Three](https://github.com/JacobGriffin21/JacobGriffin21.github.io/tree/main/Enhancement%20Three)

Vidoe Link Showing the Cloud Server Implementation: <br> [https://youtu.be/8p6fGAb_p84](https://youtu.be/8p6fGAb_p84)  



The third and final artifact, also comes from CS 340 class. This artifact and enhancement satisfies the databases category. For this artifact we created a program for an Animal Shelter that housed dogs. The program provided a dashboard to users where they could filter by the type of rescue dog they were searching for. Within the dashboard there was also a geo map that allowed the consumer to be able to see the location of all the dogs within the animal shelter. Users had the ability to create, read, update, or delete animals, this is where the program utilized the CRUD method. This program utilized a local MongoDB database the had no opportunity to scale or handle large datsets. The original database that was utilized would have to be manually scaled and downscaled, resulting in unnecessary work on the developers. 

For this enhancement, I switched the use of a local MongoDB database, to a cloud server provided by Mongo Atlas. Mongo Atlas is a cloud server that is automatically scaled and downscaled and does not require a developer to do so. The reason this enhancement is significant, is because it turned this program from a project, to an appliation that would have the ability to handle and store the information of large sets of data, and become a fully deployable and functioning app. With implementing the cloud, it took a lot of complexity out of attaching the frontend and the backend as connecting to Mongo Atlas is failry easy. This enhancement provides secuirty for the database and protects the data, it provides monitoring and alerts, scalability, easy backups, great colloboration opportunites with other developers, and even more postiive aspects. I met the course outcomes in this aritfact of demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals, and develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources. I met both of these course outcomes by providing an innovative solution and technique to bring scalability, security, and tools from the cloud server to meet industry-specific goals, and I met the second course outcome because by utilizing the cloud server as I am able to provide the built in monitoring and secuirty aspects provided by Mongo Atlas. 

### Overview of Changes for Enhancement Three
- Transformed the local MongoDB database to a cloud server provided by MongoDB Atlas
- Also able to utilize my CRUD testing in this enhancement that I implementd in Enhancement One
