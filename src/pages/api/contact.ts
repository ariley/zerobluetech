import type { APIRoute } from 'astro';
import nodemailer from 'nodemailer';

export const prerender = false;

// Initialize nodemailer with SendGrid SMTP
const transporter = nodemailer.createTransport({
  host: 'smtp.sendgrid.net',
  port: 587,
  secure: false,
  auth: {
    user: 'apikey',
    pass: import.meta.env.SENDGRID_API_KEY,
  },
});

export const POST: APIRoute = async (context) => {
  try {
    const data = await context.request.json();
    const { name, email, subject, message, turnstileToken } = data;

    // Verify Turnstile token
    if (!turnstileToken) {
      return new Response(
        JSON.stringify({ error: 'Please complete the captcha' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    const turnstileResponse = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        secret: import.meta.env.TURNSTILE_SECRET_KEY,
        response: turnstileToken,
      }),
    });

    const turnstileResult = await turnstileResponse.json();
    if (!turnstileResult.success) {
      return new Response(
        JSON.stringify({ error: 'Captcha verification failed. Please try again.' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Validate required fields
    if (!name || !email || !subject) {
      return new Response(
        JSON.stringify({ error: 'Name, email, and subject are required' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Validate email format
    if (!email.includes('@')) {
      return new Response(
        JSON.stringify({ error: 'Valid email address is required' }),
        { status: 400, headers: { 'Content-Type': 'application/json' } }
      );
    }

    if (!import.meta.env.SENDGRID_API_KEY) {
      console.log('Contact form submission (SendGrid not configured):', { name, email, subject });
      return new Response(
        JSON.stringify({ success: true, message: 'Message sent successfully' }),
        { status: 200, headers: { 'Content-Type': 'application/json' } }
      );
    }

    // Send email
    await transporter.sendMail({
      from: '"ZeroBlue Contact Form" <noreply@zerobluetech.com>',
      to: 'ariley@gmail.com',
      replyTo: email,
      subject: `[ZeroBlue Contact] ${subject}`,
      html: `
        <h2>New Contact Form Submission</h2>
        <p><strong>From:</strong> ${name} (${email})</p>
        <p><strong>Subject:</strong> ${subject}</p>
        <hr>
        <p><strong>Message:</strong></p>
        <p>${message ? message.replace(/\n/g, '<br>') : '(No message provided)'}</p>
        <hr>
        <p style="color: #666; font-size: 12px;">
          Submitted at ${new Date().toISOString()}
        </p>
      `
    });

    console.log('Contact form email sent from:', email);

    return new Response(
      JSON.stringify({ success: true, message: 'Message sent successfully' }),
      { status: 200, headers: { 'Content-Type': 'application/json' } }
    );

  } catch (error: any) {
    console.error('Error sending contact form:', error);
    return new Response(
      JSON.stringify({ error: 'Failed to send message. Please try again.' }),
      { status: 500, headers: { 'Content-Type': 'application/json' } }
    );
  }
};

