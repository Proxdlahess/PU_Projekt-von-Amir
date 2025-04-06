using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEditor;

public class GameManager : MonoBehaviour
{
    public void Menu()
    {
        Debug.Log("Bouton Menu cliqué !");
        SceneManager.LoadScene("MainMenu");
    }
}
