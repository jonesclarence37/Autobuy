const triggerProject = (z, bundle) => {
  const request = {
    url: 'http://zapier.apps.prod.nuxeo.io/nuxeo/api/v1/search/pp/default_document_suggestion/execute',
    params: {},
  };
  return z.request(request).then((response) => {
    const projects = JSON.parse(response.content).entries;
    // Test for manipulating zapier widgets
    const input = {
      key: 'example',
      type: 'string',
      required: true,
      label: 'example',
    };
    z.console.log(JSON.stringify(bundle));
    operation.inputFields.push(input);
    return projects.map((project) => {
      project.id = project.uid;
      delete project.uid;
      return project;
    });
  });
};