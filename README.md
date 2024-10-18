
# Craft Community Hub

Craft Community Hub is an e-commerce platform designed for artisans and sellers to showcase their handmade and craft products. The platform allows sellers to manage their products, track orders, view earnings, and handle customer interactions.

## Features

- **Seller Dashboard**: Manage your products, view and update orders, and track earnings.
- **Product Management**: Sellers can add, edit, and delete products.
- **Order Management**: Sellers can view customer orders, update order statuses, and see detailed order information.
- **Earnings Tracking**: Sellers can track their total earnings, pending earnings, and completed sales.
- **Customer Interaction**: Customers can browse products, add items to their cart, and place orders.

## Technologies Used

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Frontend**: HTML, CSS, JavaScript
- **Templates**: Jinja2 for dynamic HTML
- **Styling**: Font Awesome for icons, Custom CSS

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- MongoDB
- Node.js and npm (for JavaScript dependencies like Font Awesome)

### Clone the Repository

```bash
git clone https://github.com/yourusername/craft-community-hub.git
cd craft-community-hub
```

### Install Python Dependencies

Create a virtual environment and install the required Python packages:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### MongoDB Setup

Ensure MongoDB is running and create a database for the project. Update the MongoDB connection URI in your Flask application if necessary.

### Configuration

Create a `.env` file in the root of the project to store your environment variables such as MongoDB URI, secret keys, etc.

```bash
MONGO_URI=mongodb://localhost:27017/craft_community_db
SECRET_KEY=your_secret_key
```

### Run the Application

After setting everything up, start the Flask server:

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000`.

## Project Structure

```bash
craft-community-hub/
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .env                    # Environment variables (not included in repo)
```

## Features in Detail

### Seller Dashboard

Sellers can access the dashboard to manage their products and track orders and earnings.

- **Manage Products**: Add new products, edit existing products, and remove items from your catalog.
- **Track Orders**: View incoming orders, see customer details, and update the status (e.g., Pending, Shipped, Delivered).
- **Earnings Overview**: Get an overview of your total earnings, pending earnings, and completed sales.

### Order Management

- **Order Details**: View details of each order, including customer information, products, quantities, and total price.
- **Order Status Update**: Update the status of an order (e.g., Pending, Shipped, Delivered).

### Earnings Tracking

Sellers can view their earnings and breakdown per order:

- **Total Earnings**: Total amount earned from all orders.
- **Pending Earnings**: Earnings from orders that are not yet delivered.
- **Completed Sales**: Number of sales that have been delivered.

## Contributions

We welcome contributions to enhance the platform. Please follow the guidelines below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, feel free to contact us at maddy@makeskilled.com
