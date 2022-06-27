import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

class Product {
	private String name;
    private BigDecimal price;
    private int rating;
    private String author;

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    public Integer getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    @Override public String toString() {
        return "Product{" + "name='" + name + '\'' + ", price=" + price + ", rating=" + rating + '}';
    }
}

class Order {
    private List<Product> items;
    private String orderId;

    public String getOrderId() {
        return orderId;
    }

    public void setOrderId(String orderId) {
        this.orderId = orderId;
    }

    public List<Product> getItems() {
        return items;
    }

    public void setItems(List<Product> items) {
        this.items = items;
    }

    @Override public String toString() {
        return "Order{" + "items=" + items + ", orderId='" + orderId + '\'' + '}';
    }
}

class Customer {
    private String customerName;
    private List<Order> orders;

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void setOrders(List<Order> orders) {
        this.orders = orders;
    }

    @Override public String toString() {
        return "Customer{" + "customerName='" + customerName + '\'' + ", orders=" + orders + '}';
    }
}

class Main {
    static Customer customer1 = new Customer();
    static Customer customer2 = new Customer();
    
    // This list was added only for working with 6th examples and any that exists next. 
    // The previous ones were not demonstrated with this list
    static List<Product> products = new ArrayList<>();
  
  // TODO: Main method to implement
  
  // Initialization in init method
  private static void init() {
        Product product = new Product();
        product.setName("Java Programming I");
        product.setPrice(BigDecimal.valueOf(700));
        product.setAuthor("A.N.M. Bazlur Rahman");
        product.setRating(10);

        Product product1 = new Product();
        product1.setName("Java Programming II");
        product1.setPrice(BigDecimal.valueOf(300));
        product1.setAuthor("A.N.M. Bazlur Rahman");
        product1.setRating(9);

        Product product2 = new Product();
        product2.setName("Thread Programming");
        product2.setPrice(BigDecimal.valueOf(250));
        product2.setAuthor("A.N.M. Bazlur Rahman");
        product2.setRating(9);

        Product product3 = new Product();
        product3.setName("Sun Java 2");
        product3.setAuthor("Unknown Author");
        product3.setPrice(BigDecimal.valueOf(250));
        product3.setRating(7);

        products = List.of(product, product1, product2, product3);

        Order order1 = new Order();
        order1.setOrderId(UUID.randomUUID().toString());

        order1.setItems(new ArrayList<>());
        order1.getItems().add(product);
        order1.getItems().add(product1);
        order1.getItems().add(product2);
        order1.getItems().add(product3);

        Order order2 = new Order();
        order2.setOrderId(UUID.randomUUID().toString());
        order2.setItems(new ArrayList<>());
        order2.getItems().add(product3);
        order2.getItems().add(product1);
        order2.getItems().add(product);

        Order order3 = new Order();
        order3.setOrderId(UUID.randomUUID().toString());
        order3.setItems(new ArrayList<>());
        order3.getItems().add(product2);
        order3.getItems().add(product);
        order3.getItems().add(product1);

        Order order4 = new Order();
        order4.setOrderId(UUID.randomUUID().toString());
        order4.setItems(new ArrayList<>());
        order4.getItems().add(product3);
        order4.getItems().add(product1);
        order4.getItems().add(product2);

        customer1.setCustomerName("Mainul");
        List<Order> orders1 = new ArrayList<>();
        orders1.add(order1);
        orders1.add(order3);
        customer1.setOrders(orders1);

        customer2.setCustomerName("Hasan");
        List<Order> orders2 = new ArrayList<>();
        orders2.add(order2);
        orders2.add(order4);
        customer2.setOrders(orders2);
    }
}
