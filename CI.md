# Best practices for CI

1. Maintain a code repository
2. Automate the build
3. Make the build self-testing
4. Everyone commits to the baseline every day
5. Every commit (to baseline) should be built
6. Keep the build fast
7. Test in a clone of the production environment
8. Make it easy to get the latest deliverables
9. Everyone can see the results of the latest build
10. Automate deployment
11. Commit early, commit often
12. Build only once


# Jenkins Best practices
1. Keep Jenkins Secure At All Times
2. Always Backup The “JENKINS_HOME” Directory
3. Setup A Different Job/Project For Each Maintenance Or Development Branch Created
4. Prevent Resource Collisions In Jobs That Are Running In Parallel
5. Use “File Fingerprinting” To Manage Dependencies
6. Avoid Complicated Groovy Codesode In Pipelines
7. Build A Scalable Jenkins Pipeline
8. Manage Declarative Syntax/Declarative Pipelines
9. Maintain Higher Test Code Coverage & Run Unit Tests As Part Of Your Pipeline
10. Monitor Your CI/CD Pipeline