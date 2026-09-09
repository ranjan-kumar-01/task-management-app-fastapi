from typing import List

from fastapi_mail import (
    ConnectionConfig,
    FastMail,
    MessageSchema,
    MessageType,
    NameEmail,
)
from pydantic import BaseModel, EmailStr, SecretStr

from src.utils.settings import settings


class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME="ranjankumaratimi@gmail.com",
    MAIL_PASSWORD=SecretStr("ykoh ztrk ejcv nats"),
    MAIL_FROM="ranjankumaratimi@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_FROM_NAME="Ranjan",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


async def send_email(emails: List[str]):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Welcome to Task Management App</title>
    </head>

    <body style="
        margin: 0;
        padding: 0;
        background-color: #f4f7fb;
        font-family: Arial, Helvetica, sans-serif;
        color: #1f2937;
    ">

        <table
            width="100%"
            cellpadding="0"
            cellspacing="0"
            border="0"
            style="background-color: #f4f7fb; padding: 40px 15px;"
        >
            <tr>
                <td align="center">

                    <!-- Main Card -->
                    <table
                        width="100%"
                        cellpadding="0"
                        cellspacing="0"
                        border="0"
                        style="
                            max-width: 600px;
                            background-color: #ffffff;
                            border-radius: 12px;
                            overflow: hidden;
                            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
                        "
                    >

                        <!-- Header -->
                        <tr>
                            <td
                                align="center"
                                style="
                                    background: linear-gradient(
                                        135deg,
                                        #4f46e5,
                                        #7c3aed
                                    );
                                    padding: 35px 30px;
                                "
                            >
                                <div style="
                                    display: inline-block;
                                    width: 56px;
                                    height: 56px;
                                    line-height: 56px;
                                    border-radius: 14px;
                                    background-color: rgba(255,255,255,0.15);
                                    color: #ffffff;
                                    font-size: 28px;
                                    font-weight: bold;
                                    margin-bottom: 15px;
                                ">
                                    ✓
                                </div>

                                <h1 style="
                                    margin: 0;
                                    color: #ffffff;
                                    font-size: 28px;
                                    line-height: 36px;
                                    font-weight: 700;
                                ">
                                    Welcome to Task Management App
                                </h1>

                                <p style="
                                    margin: 10px 0 0;
                                    color: #e0e7ff;
                                    font-size: 15px;
                                    line-height: 24px;
                                ">
                                    Your account has been created successfully.
                                </p>
                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td style="padding: 40px 35px 30px;">

                                <p style="
                                    margin: 0 0 18px;
                                    font-size: 18px;
                                    font-weight: 600;
                                    color: #111827;
                                ">
                                    Hello 👋
                                </p>

                                <p style="
                                    margin: 0 0 18px;
                                    font-size: 15px;
                                    line-height: 26px;
                                    color: #4b5563;
                                ">
                                    Thank you for creating an account with
                                    <strong style="color: #111827;">
                                        Task Management App
                                    </strong>.
                                </p>

                                <p style="
                                    margin: 0 0 25px;
                                    font-size: 15px;
                                    line-height: 26px;
                                    color: #4b5563;
                                ">
                                    You can now start organizing your tasks,
                                    tracking your progress, and keeping
                                    everything in one place.
                                </p>

                                <!-- Success Box -->
                                <table
                                    width="100%"
                                    cellpadding="0"
                                    cellspacing="0"
                                    border="0"
                                    style="
                                        background-color: #f0fdf4;
                                        border: 1px solid #bbf7d0;
                                        border-radius: 8px;
                                        margin-bottom: 25px;
                                    "
                                >
                                    <tr>
                                        <td style="padding: 18px 20px;">

                                            <p style="
                                                margin: 0 0 6px;
                                                color: #166534;
                                                font-size: 14px;
                                                font-weight: 700;
                                            ">
                                                ✓ Registration successful
                                            </p>

                                            <p style="
                                                margin: 0;
                                                color: #15803d;
                                                font-size: 13px;
                                                line-height: 21px;
                                            ">
                                                Your account is ready to use.
                                            </p>

                                        </td>
                                    </tr>
                                </table>

                                <!-- CTA -->
                                <table
                                    cellpadding="0"
                                    cellspacing="0"
                                    border="0"
                                    width="100%"
                                >
                                    <tr>
                                        <td align="center">

                                            <a
                                                href="http://127.0.0.1:8000/docs"
                                                style="
                                                    display: inline-block;
                                                    background-color: #4f46e5;
                                                    color: #ffffff;
                                                    text-decoration: none;
                                                    padding: 13px 28px;
                                                    border-radius: 7px;
                                                    font-size: 14px;
                                                    font-weight: 600;
                                                "
                                            >
                                                Get Started
                                            </a>

                                        </td>
                                    </tr>
                                </table>

                                <p style="
                                    margin: 28px 0 0;
                                    font-size: 13px;
                                    line-height: 21px;
                                    color: #6b7280;
                                    text-align: center;
                                ">
                                    If you did not create this account,
                                    please contact our support team.
                                </p>

                            </td>
                        </tr>

                        <!-- Divider -->
                        <tr>
                            <td style="padding: 0 35px;">
                                <div style="
                                    height: 1px;
                                    background-color: #e5e7eb;
                                "></div>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td
                                align="center"
                                style="padding: 25px 30px 30px;"
                            >

                                <p style="
                                    margin: 0 0 8px;
                                    font-size: 13px;
                                    font-weight: 600;
                                    color: #374151;
                                ">
                                    Task Management App
                                </p>

                                <p style="
                                    margin: 0 0 8px;
                                    font-size: 12px;
                                    color: #9ca3af;
                                    line-height: 20px;
                                ">
                                    Organize your work. Stay productive.
                                </p>

                                <p style="
                                    margin: 0;
                                    font-size: 11px;
                                    color: #9ca3af;
                                ">
                                    © 2026 Task Management App. All rights reserved.
                                </p>

                            </td>
                        </tr>

                    </table>

                </td>
            </tr>
        </table>

    </body>
    </html>
    """

    message = MessageSchema(
        subject="Welcome to Task Management App",
        recipients=[NameEmail(name="", email=email) for email in emails],
        body=html,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)

    await fm.send_message(message)

    return {"message": "Email has been sent successfully"}
