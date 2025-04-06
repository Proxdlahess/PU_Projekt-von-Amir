using System.Collections;
using UnityEngine;
using UnityEngine.UI; // Pour UI Text
using TMPro; // Pour TextMeshPro

public class PlayerMouvement : MonoBehaviour
{
    [SerializeField] private TextMeshProUGUI WINTEXT; // Utilisation de TMP, change en Text si besoin

    private float horizontal;
    private float speed = 8f;
    private float jumpingPower = 16f;
    private bool isFacingRight = true;
    private bool canJump = true;

    private bool canDash = true;
    private bool isDashing;
    private float dashingPower = 24f;
    private float dashingTime = 0.2f;
    private float dashingCooldown = 1f;

    [SerializeField] private Rigidbody2D rb;
    [SerializeField] private Transform groundCheck;
    [SerializeField] private LayerMask groundLayer;
    [SerializeField] private TrailRenderer tr;

    private void Start()
    {
        // Désactiver le texte de victoire au début
        if (WINTEXT != null)
        {
            WINTEXT.gameObject.SetActive(false);
        }
    }

    private void Update()
    {
        if (isDashing) return;

        horizontal = Input.GetAxisRaw("Horizontal");

        if (Input.GetButtonDown("Jump") && canJump)
        {
            rb.velocity = new Vector2(rb.velocity.x, jumpingPower);
            canJump = false;
        }

        if (Input.GetButtonUp("Jump") && rb.velocity.y > 0f)
        {
            rb.velocity = new Vector2(rb.velocity.x, rb.velocity.y * 0.5f);
        }

        if (Input.GetKeyDown(KeyCode.LeftShift) && canDash)
        {
            StartCoroutine(Dash());
        }

        Flip();
    }

    private void FixedUpdate()
    {
        if (!isDashing)
        {
            rb.velocity = new Vector2(horizontal * speed, rb.velocity.y);
        }

        if (IsGrounded())
        {
            canJump = true;
        }
    }

    private bool IsGrounded()
    {
        return Physics2D.OverlapCircle(groundCheck.position, 0.2f, groundLayer);
    }

    private void Flip()
    {
        if ((isFacingRight && horizontal < 0f) || (!isFacingRight && horizontal > 0f))
        {
            isFacingRight = !isFacingRight;
            Vector3 localScale = transform.localScale;
            localScale.x *= -1f;
            transform.localScale = localScale;
        }
    }

    private IEnumerator Dash()
    {
        canDash = false;
        isDashing = true;
        float originalGravity = rb.gravityScale;
        rb.gravityScale = 0f;
        rb.velocity = new Vector2(transform.localScale.x * dashingPower, 0f);
        tr.emitting = true;
        yield return new WaitForSeconds(dashingTime);
        tr.emitting = false;
        rb.gravityScale = originalGravity;
        isDashing = false;
        yield return new WaitForSeconds(dashingCooldown);
        canDash = true;
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.CompareTag("Win"))
        {
            if (WINTEXT != null)
            {
                WINTEXT.gameObject.SetActive(true);
                Time.timeScale = 0;
            }
        }
    }
}
