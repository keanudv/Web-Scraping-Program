<h1>Web Scraping Program</h1>
<h2>By Keanu Valencia</h2>
<br>
<h3>Description</h3>
<p>This program allows you scrape product name and price data from a given webpage.</p>
<br>
<h3>How to Use It</h3>
<P>To use this program, you have to call the scrape_data() function and pass four parameters:</p>
<ol>
      <li>The target webpage URL.</li>
      <li>The HTML name tag.</li>
      <li>The HTML name class.</li>
      <li>The HTML price tag.</li>
      <li>The HTML price name.</li>
</ol>
<br>
<h3>Example</h3>
<p>For the Costco webpage, you need to obtain the URL, product name tag and class, and product price tag and class by inspecting the HTML code.</p>
<br>
<P>Once you have that information, you can call the scrape_data() function as pass those values as parameters (see the code below).</P>
<br>
<P>scrape_data(url="https://www.costco.com/diet-nutrition.html", name_tag="span", name_class="description", price_tag="div", price_class="price")</P>
<br>
<h3>Limitations</h3>
<P>Some websites use JavaScript to dynamically load data. The packages used in this program (Requests and BeautifulSoup) cannot execute JavaScipt. Therefore, the program may fail to retrieve data.</P><br>
<P>In addition, this program can only scrape data from one webpage at a time (Pagination). Therefore, the program will fail to retrieve data from multiple webpages.</P>
<br>
<h3>Improvements</h3>
<P>To overcome these limitations, I will expand the program to use Selenium. Selenium is a package that automates a web browser to load JavaScipt and flip to the next page or load more data.</P>
