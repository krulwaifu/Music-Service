
const PostsData = [
{
  "category": "Hip-hop",
  "title": "Morgenshtern",
  "text": "Russian rapper, record producer, and songwriter Alisher Morgenshtern.",
  "image": "https://upload.wikimedia.org/wikipedia/en/a/aa/Pososi.jpg" },

{
  "category": "Hip-hop",
  "title": "Irina Kairatovna",
  "text": "Kazakh creative group that has been founded in Almaty.",
  "image": "https://i.scdn.co/image/dd1f8df23ffa95e726c85cced437944fd214a2f8" },

{
  "category": "Jpop",
  "title": "Kana-boon",
  "text": "Kana-Boon are a Japanese rock band formed in 2008. Doppel being their best-charting album, reaching the third place on the chart.",
  "image": "https://pbs.twimg.com/profile_images/1309690542905679872/pllFHWmS_400x400.jpg" }];



class Main extends React.Component {
  constructor() {
    super();

    this.state = {
      posts: {} };

  }
  componentWillMount() {
    this.setState({
      posts: PostsData });

  }


  render() {
    return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/
    React.createElement("header", { className: "app-header" }), /*#__PURE__*/
    React.createElement(Title, null), /*#__PURE__*/
    React.createElement("div", { className: "app-card-list", id: "app-card-list" },

    Object.
    keys(this.state.posts).
    map(key => /*#__PURE__*/React.createElement(Card, { key: key, index: key, details: this.state.posts[key] }))));



  }}



class Title extends React.Component {
  render() {
    return /*#__PURE__*/React.createElement("section", { className: "app-title" }, /*#__PURE__*/
    React.createElement("div", { className: "app-title-content" }, /*#__PURE__*/
    React.createElement("h1", null, "Latest Releases"), /*#__PURE__*/
    React.createElement("p", null, "May 2020"), /*#__PURE__*/));
  }}



class Button extends React.Component {
  render() {
    return /*#__PURE__*/(
      React.createElement("button", { className: "button button-primary" }, /*#__PURE__*/
      React.createElement("i", { className: "fa fa-chevron-right" }), "Listen"));


  }}



class CardHeader extends React.Component {
  render() {
    const { image, category } = this.props;
    var style = {
      backgroundImage: 'url(' + image + ')' };

    return /*#__PURE__*/(
      React.createElement("header", { style: style, className: "card-header" }, /*#__PURE__*/
      React.createElement("h4", { className: "card-header--title" }, category)));


  }}



class CardBody extends React.Component {
  render() {
    return /*#__PURE__*/(
      React.createElement("div", { className: "card-body" }, /*#__PURE__*/
      React.createElement("p", { className: "date" }, "March 20 2015"), /*#__PURE__*/

      React.createElement("h2", null, this.props.title), /*#__PURE__*/

      React.createElement("p", { className: "body-content" }, this.props.text), /*#__PURE__*/

      React.createElement(Button, null)));


  }}



class Card extends React.Component {
  render() {
    return /*#__PURE__*/(
      React.createElement("article", { className: "card" }, /*#__PURE__*/
      React.createElement(CardHeader, { category: this.props.details.category, image: this.props.details.image }), /*#__PURE__*/
      React.createElement(CardBody, { title: this.props.details.title, text: this.props.details.text })));


  }}



ReactDOM.render( /*#__PURE__*/
React.createElement(Main, null),
document.getElementById('app'));