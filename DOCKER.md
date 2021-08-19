# Docker Best Practices 

1. Avoid unnecessary privileges
2. Make executables owned by root and not writable
3. Use multistage builds
4. Use smallest images 
5. Try to mininize layers
6. Use trusted base images
7. Prevent confidential data leaks - do not put secrets inside the image/code
8. Build context and dockerignore
9. Use linters/SAST analysers
10. Use Fixed Tags for Immutability
11. Pass sensitive data to the container via secrets arguments
