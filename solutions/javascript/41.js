function itinerary(travel, separator = "-") {
  let airports = [];
  for (let index = 0; index < travel.length; ++index) {
    airports.push(travel[index].in);
    if (index == travel.length - 1 || travel[index].out != travel[index + 1].in) {
      airports.push(travel[index].out);
    }
  }
  return airports.join(separator);
}