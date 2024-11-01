<h1>Web Scraping Program</h1>
<h2>By Keanu Valencia</h2>
<br>
<h3>Description</h3>
<p>This program allows you scrape product name and price data from a given webpage.</p>
<br>
<h3>How to Use It</h3>
<P>To use this program, you have to call the scrape_data() function and pass four parameters:</p>
<ol>
      <li>The target webpage URL</li>
      <li>The HTML name tag</li>
      <li>The HTML name class</li>
      <li>The HTML price tag</li>
      <li>The HTML price name</li>
</ol>
<br>
<h3>Example</h3>
<p>For the Costco webpage, you need to obtain the URL, product name tag and class, and the price tag and class by inspecting the HTML code.</p>
<P>Once you have that information, you can call the scrape_data() function as pass those values as parameters</P>
<br>

scrape_data(url="", name_tag="", name_class="", price_tag="", price_class="")

<br>
<h3>Limitations</h3>
<P>Some websites use JavaScript to dynamically load data. The packages used in this program (Requests and BeautifulSoup) cannot execute JavaScipt. Therefore, the program may fail to retrieve data.</P><br>
<P>This program can only scrape data from one page (Pagination). Data for all products exist on multiple pages. Therefore, the program will fail to retrieve all product data.</P>
<br>
<h3>Improvements</h3>
<P>To overcome these limitations, I will expand the program to use Selenium. Selenium is a package that automates a web browser to load JavaScipt and flip to the next page or load more data.</P>
