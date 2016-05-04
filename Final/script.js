'use strict';
// Depending on the URL argument, render as LTR or RTL.
var rtl = (document.location.search == '?rtl');
var workspace = null;

function start() {
  var toolbox = document.getElementById('toolbox');
  workspace = Blockly.inject('blocklyDiv',
          {comments: true,
           disable: true,
           collapse: true,
           grid:
             {spacing: 25,
              length: 3,
              colour: '#ccc',
              snap: true},
           maxBlocks: Infinity,
           media: 'media/',
           readOnly: false,
           rtl: rtl,
           scrollbars: true,
           toolbox: toolbox,
           zoom:
             {controls: true,
              wheel: true,
              startScale: 1.0,
              maxScale: 4,
              minScale: .25,
              scaleSpeed: 1.1
             },
          });
  // Restore previously displayed text.
  var text = sessionStorage.getItem('textarea');
  if (text) {
    document.getElementById('importExport').value = text;
  }
  taChange();
  // Restore event logging state.
  var state = sessionStorage.getItem('logEvents');
}

function toXml() {
  var output = document.getElementById('importExport');
  var xml = Blockly.Xml.workspaceToDom(workspace);
  output.value = Blockly.Xml.domToPrettyText(xml);
  output.focus();
  output.select();
  taChange();
}

function fromXml() {
  var input = document.getElementById('importExport');
  var xml = Blockly.Xml.textToDom(input.value);
  Blockly.Xml.domToWorkspace(workspace, xml);
  taChange();
}

function toCode(lang) {
  var output = document.getElementById('importExport');
  output.value = Blockly[lang].workspaceToCode(workspace);
  taChange();
}

// Disable the "Import from XML" button if the XML is invalid.
// Preserve text between page reloads.
function taChange() {
  var textarea = document.getElementById('importExport');
  sessionStorage.setItem('textarea', textarea.value)
  var valid = true;
  try {
    Blockly.Xml.textToDom(textarea.value);
  } catch (e) {
    valid = false;
  }
  document.getElementById('import').disabled = !valid;
}



function logger(e) {
  console.log(e);
}
