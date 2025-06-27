function ArtistCard({ artist }) {
  const price = artist.skills && artist.skills[0] && artist.skills[0].default_amount;
  const status = artist.acceptable ? `Open - Price: ${price || '?'}` : 'Closed';
  const statusClass = artist.acceptable ? 'status open' : 'status closed';
  return React.createElement(
    'div',
    { className: 'card' },
    React.createElement('div', { className: 'name' }, artist.name),
    React.createElement('div', { className: statusClass }, status)
  );
}

function App() {
  const [artists, setArtists] = React.useState([]);

  React.useEffect(() => {
    fetch('/api/artists')
      .then(res => res.json())
      .then(data => setArtists(data));
  }, []);

  return React.createElement(
    'div',
    { className: 'container' },
    React.createElement('h1', null, 'Followed Artists'),
    artists.map(a => React.createElement(ArtistCard, { artist: a, key: a.screen_name }))
  );
}

ReactDOM.render(React.createElement(App), document.getElementById('root'));
