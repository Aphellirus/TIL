#include <iostream>
#include <ctime>
#include <cstdlib>

int main()
{
    srand(time(0));
    
    int season = 1 + rand() % 4;
    
    int episode;
    
    if (season == 1)
    {
        episode = 1 + rand() % 11;
    }
    else if (season == 4)
    {
        episode = 1 + rand() % 5;
    }
    else
    {
        episode = 1 + rand() % 10;
    }
    
    std::cout<< "Rick and Morty\n";
    std::cout<< "---------------\n";
    std::cout<< "Today you shoud watch,\n";
    std::cout<< "Season "<< season<< " Episode "<< episode << std::endl;
    
    return 0;
}
