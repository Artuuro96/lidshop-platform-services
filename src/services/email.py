import smtplib
from email.mime.text import MIMEText

from decouple import config
from jinja2 import Template

from src.repositories.client import get_client_by_id
from src.schemas.sale import SaleSchema


async def send_email(sale: SaleSchema):
    client = await get_client_by_id(sale["clientId"])
    sender_email = config("SENDER_EMAIL")
    sender_password = config("PASSWORD_SENDER_EMAIL")
    recipient_email = client["email"]
    subject = "Tu Compra en LID Shop"
    body = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tu compra en LID Shop</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 0;
                color: #333;
            }
            .email-container {
                width: 100%;
                max-width: 600px;
                margin: 0 auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            .header {
                text-align: center;
                margin-bottom: 20px;
            }
            .header img {
                max-width: 150px;
                border-radius: 10px;
            }
            .message {
                font-size: 18px;
                text-align: center;
                margin-top: 20px;
                color: #333;
            }
            .footer {
                text-align: center;
                font-size: 14px;
                color: #888;
                margin-top: 40px;
            }
            .button {
                background-color: #f2c94c;
                color: white;
                padding: 12px 20px;
                font-size: 16px;
                text-decoration: none;
                border-radius: 5px;
                display: block;
                margin: 30px auto 0;
                text-align: center;
                width: 200px;
            }
            .button:hover {
                background-color: #e0b24b;
            }
    
            .table-container {
                margin-top: 30px;
            }
    
            h3 {
                text-align: center;
                font-size: 24px;
                color: #333;
                margin-bottom: 15px;
            }
    
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                background-color: #fff;
            }
    
            th, td {
                padding: 12px 15px;
                text-align: left;
                border: 1px solid #ddd;
                font-size: 16px;
            }
    
            th {
                background-color: #333;
                color: #fff;
                font-weight: bold;
            }
    
            tbody tr:nth-child(even) {
                background-color: #f2f2f2;
            }
    
            tbody tr:hover {
                background-color: #f0a500;
            }
    
            tbody td {
                color: #333;
            }
    
            tbody tr {
                transition: background-color 0.3s ease;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <a href="https://ibb.co/2Yd8d0Rd">
                    <img src="https://i.ibb.co/rfHbHKqH/lidshop.jpg" alt="lidshop" border="0" />
                </a>
            </div>
            <div class="message">
                <h2>¡Gracias por tu compra!</h2>
                <p>
                    Querido {{client.name}}, estamos encantados de que hayas elegido nuestro producto. 
                    Tu compra ha sido procesada con éxito y se te agendará una fecha de entrega a la brevedad.
                </p>
                <p>A continuación te mostramos un resumen de tus pagos y detalles de tu compra:</p>
            </div>
    
            <!-- Resumen de Pagos -->
            <div class="table-container">
                <h3>Resumen de Pagos</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Cantidad</th>
                            <th>Fecha</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for sale in sale.scheduledPayments %}
                        <tr>
                            <td>${{ sale.quantity }}</td>
                            <td>{{ sale.dateToPay[:10] }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
    
            <!-- Resumen de Artículos -->
            <div class="table-container">
                <h3>Resumen de Artículos</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Artículo</th>
                            <th>Cantidad</th>
                            <th>Precio Unitario</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for article in sale.articles %}
                        <tr>
                            <td>{{ article.code }}</td>
                            <td>{{ article.name }}</td>
                            <td>${{ article.lidShopPrice }}</td>
                            <td>${{ 2 * article.lidShopPrice }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
    
            <div class="footer">
                <p>Gracias por confiar en nosotros.</p>
                <p>¡Te esperamos de vuelta!</p>
            </div>
        </div>
    </body>
    </html>
    """
    template = Template(body)
    html_output = template.render(sale=sale, client=client)
    html_message = MIMEText(html_output, 'html')
    html_message['Subject'] = subject
    html_message['From'] = sender_email
    html_message['To'] = recipient_email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, html_message.as_string())
