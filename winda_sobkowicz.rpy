I-Logix-RPY-Archive version 8.14.0 C++ 9810313
{ IProject 
	- _id = GUID 92afcd37-0120-45c4-af7f-32bfb06f6b06;
	- _myState = 8192;
	- _name = "winda_sobkowicz";
	- _modifiedTimeWeak = 9.8.2018::23:56:37;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _name = "Default";
		- _id = GUID 8bbbc81d-41fc-408b-82d8-7912254c4a0c;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _name = "DefaultComponent";
		- _id = GUID b8fa7e17-4a08-4c6e-ab84-a52542b14e82;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 3;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID 8bbbc81d-41fc-408b-82d8-7912254c4a0c;
		}
		{ IProfile 
			- fileName = "UMLPerspectives";
			- _persistAs = "$OMROOT\\Settings\\UMLPerspectives";
			- _id = GUID d24d9192-bc4f-48a2-a4e1-fdaebbdfa6b6;
			- _partOfTheModelKind = referenceunit;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID 0185a140-e3c8-45fe-b3ad-591596c42673;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 3;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 3;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Composition";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "MarkMisplacedElements";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "ObjectModelGe";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "ShowAttributes";
										- _Value = "Explicit";
										- _Type = Enum;
										- _ExtraTypeInfo = "All,None,Public,Explicit";
									}
									{ IProperty 
										- _Name = "ShowName";
										- _Value = "Relative";
										- _Type = Enum;
										- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
									}
									{ IProperty 
										- _Name = "ShowOperations";
										- _Value = "Public";
										- _Type = Enum;
										- _ExtraTypeInfo = "All,None,Public,Explicit";
									}
									{ IProperty 
										- _Name = "ShowStereotype";
										- _Value = "Label";
										- _Type = Enum;
										- _ExtraTypeInfo = "Label,Bitmap,None";
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Complete";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Complete_Relation";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Composition";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "ShowSourceRole";
										- _Value = "False";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "ShowTargetRole";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "ShowName";
										- _Value = "Label";
										- _Type = Enum;
										- _ExtraTypeInfo = "Full_path,Relative,Name_only,Label";
									}
								}
							}
						}
					}
				}
			}
			- _name = "Model1";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "9.8.2018::23:57:20";
			- _graphicChart = { CGIClassChart 
				- _id = GUID f5b7ec9d-a196-4dae-a398-aad6838cf382;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 0185a140-e3c8-45fe-b3ad-591596c42673;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 20;
				{ CGIClass 
					- _id = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "TopLevel";
						- _id = GUID 493ec7a0-7a09-479e-8297-0eac132bcd7a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID e99b9150-6f27-4126-9f16-98a0252c0b20;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 8e6c812f-ca33-4a86-abac-d88a43cdd297;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 73f38564-8009-40b7-a24a-7b3b22dc084e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "drzwi";
						- _id = GUID d0c8d554-3bc9-488c-af2e-ac424e80d0eb;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "drzwi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2632;
					- m_transform = 0.0793201 0 0 0.101604 189.841 458.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 96b00735-0911-439e-8c8b-9d52ddbcb45f;
							- m_name = "Attribute";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
						{ CGICompartment 
							- _id = GUID a6143d4d-dd9a-43ae-8bd2-eb2f4ee914b5;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 680f7125-9ef0-49a0-a747-5afea76ec225;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "Attribute,Operation,Part,";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "sterownik";
						- _id = GUID fbbd13e7-bc1d-4e28-a03f-c2fa8bb5bb08;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "sterownik";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.11898 0 0 0.136363 189.762 -14.8636 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=33%,33%,33%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>
<frame name=PartListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ CGICompartment 
							- _id = GUID a87c86d9-29ee-4af1-8c86-53d76e56e4e4;
							- m_name = "Attribute";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
						{ CGICompartment 
							- _id = GUID 74b9a1a8-49bf-45e7-b0fb-0c73513c6c86;
							- m_name = "Operation";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- _itemValueOfFontPropertiesMapCount = 1;
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
						}
						{ CGICompartment 
							- _id = GUID 09c581a0-17ed-4f0e-9f1c-c5e55ee22222;
							- m_name = "Part";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- _itemValueOfFontPropertiesMapCount = 2;
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID d92d00a4-05dd-4ed4-a9f7-8cf6b88eb5d0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "klawiatura";
						- _id = GUID 0776c213-9b0b-45d4-b750-d4575f09e66f;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "klawiatura";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2632;
					- m_transform = 0.0793201 0 0 0.101604 -0.15863 245.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 7d3921a9-fadc-491a-8ec1-7dc654db2853;
							- m_name = "Attribute";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
						{ CGICompartment 
							- _id = GUID 66b0823c-e710-46e0-bc6a-e69a2db3748b;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID c5d32093-1f0c-4f77-8c83-6967b0720a29;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "wyswietlacz";
						- _id = GUID 9e9abcec-a90b-45cb-9e5e-0a4b47ce1fef;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "wyswietlacz";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2632;
					- m_transform = 0.0802644 0 0 0.101604 364.839 282.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID d6e8cdf4-9350-4939-8491-2ea7e50c1dd2;
							- m_name = "Attribute";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
						{ CGICompartment 
							- _id = GUID bc64147d-a7a4-4bb3-b789-b593b0e6f65a;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 1581e3c9-05be-4ee5-9736-d573a41b3aef;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "hamulec";
						- _id = GUID 9dc7299e-a479-48c0-b86c-abf8f90b6068;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "hamulec";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2824;
					- m_transform = 0.0793201 0 0 0.101604 245.841 300.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID db98e462-7675-4383-93d5-41dbaaabc76f;
							- m_name = "Attribute";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
						{ CGICompartment 
							- _id = GUID 26d834e6-7984-4cd0-a7c3-fa21f2135281;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID cde37b4b-3b73-4972-9bba-364c53ce4ece;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "winda";
						- _id = GUID 775a0b6c-c377-44dd-bd66-aa2f31e8270b;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "winda";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2632;
					- m_transform = 0.11898 0 0 0.136363 364.762 -14.8636 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID d382fd9f-aa54-4804-b6e1-55d503ba3e24;
							- m_name = "Attribute";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
						{ CGICompartment 
							- _id = GUID 68fd6e77-e34a-4c1b-85db-1a6830dbd456;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 7975e8c1-4366-4a2b-a2c3-aecdc2574a88;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 36;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "winda";
						- _name = "itsSterownik_2";
						- _id = GUID 2a9eadb0-c3fd-4297-b20b-e4c22768a81f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cde37b4b-3b73-4972-9bba-364c53ce4ece;
					- m_sourceType = 'F';
					- m_pTarget = GUID 680f7125-9ef0-49a0-a747-5afea76ec225;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 2 784 ;
					- m_TargetPort = 1061 784 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "sterownik";
						- _name = "itsWinda_2";
						- _id = GUID 4f892a53-721f-4879-9b13-354a627f8dbd;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = -7;
						- m_nOrientationCtrlPt = 4;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID d412c652-8767-4be4-a52e-4f40cfff421a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "silnik";
						- _id = GUID b42e513c-8448-49fe-aa0b-a85aa316b703;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "silnik";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2568;
					- m_transform = 0.151086 0 0 0.198752 -0.302185 426.611 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=21%,79%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 5cd2c238-ed25-49bc-a6da-50f9159b7ccb;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 1d89166f-67c8-493c-a952-ddbd719a796d;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID efe892de-ea29-435e-bf16-be61329d5386;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "modul";
						- _id = GUID e0a7c89e-5117-4e24-b578-3d8fd507fec6;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "modul";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2152;
					- m_transform = 0.136922 0 0 0.155971 5.72616 -17.3146 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID a8934b10-2615-40ce-b637-262eefa220f5;
							- m_name = "Attribute";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- _itemValueOfFontPropertiesMapCount = 3;
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
						}
						{ CGICompartment 
							- _id = GUID 120001ae-87e3-4482-9ea1-afc62ef8f6e7;
							- m_name = "Operation";
							- m_displayOption = All;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- _itemValueOfFontPropertiesMapCount = 4;
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
							- _fontPropValues = "Tahoma 8 400 0 0 0 0";
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 7b41ea55-38bb-48d0-ad1e-6e9e704ff8a0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "klawiatura";
						- _name = "modul";
						- _id = GUID 2f3a728f-b1ee-407d-a730-8bac34375dca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d92d00a4-05dd-4ed4-a9f7-8cf6b88eb5d0;
					- m_sourceType = 'F';
					- m_pTarget = GUID efe892de-ea29-435e-bf16-be61329d5386;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 557 329 ;
					- m_TargetPort = 280 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID bd6d2950-2ca9-4573-a0ed-e69c612be4a5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "drzwi";
						- _name = "modul";
						- _id = GUID e77ca0be-2c69-4930-9fbc-aa245c194c2f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 73f38564-8009-40b7-a24a-7b3b22dc084e;
					- m_sourceType = 'F';
					- m_pTarget = GUID efe892de-ea29-435e-bf16-be61329d5386;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 973 329 ;
					- m_TargetPort = 878 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 3932b314-62df-4dc3-8fa4-112f695e4db4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "hamulec";
						- _name = "modul";
						- _id = GUID 305d7b51-d9ed-4f50-8da3-ac995e1dddd5;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1581e3c9-05be-4ee5-9736-d573a41b3aef;
					- m_sourceType = 'F';
					- m_pTarget = GUID efe892de-ea29-435e-bf16-be61329d5386;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 531 329 ;
					- m_TargetPort = 1054 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 5c31a3e6-f191-40c9-a710-de498612e075;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "wyswietlacz";
						- _name = "modul";
						- _id = GUID e9a5f323-8b70-4cbd-b4ce-72128db12b92;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID c5d32093-1f0c-4f77-8c83-6967b0720a29;
					- m_sourceType = 'F';
					- m_pTarget = GUID efe892de-ea29-435e-bf16-be61329d5386;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 550 319 ;
					- m_TargetPort = 1061 1329 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4082126d-913e-490f-aa02-089b336f9188;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "silnik";
						- _name = "modul";
						- _id = GUID 2018e73e-cf2d-41f0-9292-678f49e6fe71;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID d412c652-8767-4be4-a52e-4f40cfff421a;
					- m_sourceType = 'F';
					- m_pTarget = GUID efe892de-ea29-435e-bf16-be61329d5386;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 591 329 ;
					- m_TargetPort = 681 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAssociationEnd 
					- _id = GUID 004559c3-c944-43e6-b6a6-79d338782263;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 36;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "sterownik";
						- _name = "itsHamulec";
						- _id = GUID 05fc0aef-668f-490f-8aa4-4a0f0aab0b48;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 680f7125-9ef0-49a0-a747-5afea76ec225;
					- m_sourceType = 'F';
					- m_pTarget = GUID 1581e3c9-05be-4ee5-9736-d573a41b3aef;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 952 1451 ;
					- m_TargetPort = 721 329 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "hamulec";
						- _name = "itsSterownik";
						- _id = GUID 2cc7674a-8559-420f-9fe0-5689dea48393;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID a348163c-c04f-409a-accd-20fa1440be39;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 36;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "sterownik";
						- _name = "itsDrzwi";
						- _id = GUID d5515ff1-6290-41ea-ac21-ff273f9d8fd2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 680f7125-9ef0-49a0-a747-5afea76ec225;
					- m_sourceType = 'F';
					- m_pTarget = GUID 73f38564-8009-40b7-a24a-7b3b22dc084e;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 330 1451 ;
					- m_TargetPort = 494 329 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "drzwi";
						- _name = "itsSterownik";
						- _id = GUID c5c048dd-e123-4bd5-8116-4df9578376f8;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 693d0819-e4b6-42a1-8d37-d1e5c439a8f9;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 36;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "sterownik";
						- _name = "itsSilnik";
						- _id = GUID 6684476b-796c-4ecf-9cf9-e62fef2640ea;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 680f7125-9ef0-49a0-a747-5afea76ec225;
					- m_sourceType = 'F';
					- m_pTarget = GUID d412c652-8767-4be4-a52e-4f40cfff421a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 199 413  115 413  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 78 1451 ;
					- m_TargetPort = 763 324 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "silnik";
						- _name = "itsSterownik";
						- _id = GUID 2753ecb0-3a65-4085-9022-164b328ef521;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID 5219ef32-4295-4e95-876e-56c21e23a4b8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "parametry";
						- _id = GUID c27f2f6f-18df-4ad5-a463-4103b2f1d9c1;
					}
					- m_pParent = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
					- m_name = { CGIText 
						- m_str = "parametry";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2568;
					- m_transform = 0.0793201 0 0 0.101604 511.841 254.572 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 320c416c-a086-4a0c-8f46-a974ee067b63;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 49ce5ea7-5c87-4bfc-b01b-67d0ce91afde;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID d7192f96-51a1-45be-a755-9653ee157132;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 36;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "winda";
						- _name = "itsParametry";
						- _id = GUID 61a95442-a003-4a6a-a2f3-08323d240405;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cde37b4b-3b73-4972-9bba-364c53ce4ece;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5219ef32-4295-4e95-876e-56c21e23a4b8;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 456 235  556 235  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 767 1451 ;
					- m_TargetPort = 557 329 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _subsystem = "Default";
						- _class = "parametry";
						- _name = "itsWinda";
						- _id = GUID 5f50ece7-b1e0-4458-a03a-0d85e7a272e5;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "*";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID d2b833ee-9e62-46b9-8b4b-9d134a1bcf29;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
				- m_bFreezeCompartmentContent = 0;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _name = "Default";
				- _id = GUID 8bbbc81d-41fc-408b-82d8-7912254c4a0c;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID b8fa7e17-4a08-4c6e-ab84-a52542b14e82;
		}
	}
	- UCDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IUCDiagram 
			- _id = GUID 142d6753-6927-41a3-a614-6f1ae386d883;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,53,142";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "2";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "UseCase";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,140,65";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "MarkMisplacedElements";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Funkcje in Dafault";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "9.8.2018::23:56:28";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 7bd61c14-eb76-40d4-a167-5aa7d237f717;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IUCDiagram";
					- _id = GUID 142d6753-6927-41a3-a614-6f1ae386d883;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 37;
				{ CGIClass 
					- _id = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _subsystem = "Default";
						- _name = "TopLevel";
						- _id = GUID 493ec7a0-7a09-479e-8297-0eac132bcd7a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 3fc6ec0b-de68-4eed-964a-76189d364bf3;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID cd1e9af0-4471-43e2-a8bb-94ac89b704d5;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIBasicClass 
					- _id = GUID d5f08a73-b4dc-458d-b426-efd190717ec2;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _subsystem = "Default";
						- _name = "operator";
						- _id = GUID 252d5bda-2726-42c1-912a-768009eb88ae;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "operator";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0489381 0 0 0.124343 1.38689 251.665 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID cb24c3af-a8dd-491d-ae3c-16a2dd8926d2;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _subsystem = "Default";
						- _name = "uzytkownik";
						- _id = GUID 9dab12a5-bbf1-473d-a6ea-a83870e9e16b;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "uzytkownik";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0489381 0 0 0.124343 215.387 27.6655 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 6da1f81c-23ed-404d-aa4c-f35e14063024;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _subsystem = "Default";
						- _name = "serwisant";
						- _id = GUID d8f083c8-366a-47ef-9a40-4c364fbaa655;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "serwisant";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0489381 0 0 0.124343 215.387 189.665 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 20082586-8c00-4409-8542-a84f814c1159;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _subsystem = "Default";
						- _name = "system";
						- _id = GUID ad9886f8-90bc-4c40-8701-93dad873e82e;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "system";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0489381 0 0 0.124343 100.387 420.665 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID da6c9790-1c6a-4a21-acbc-f784aee24dbf;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "system";
						- _name = "operator";
						- _id = GUID fe21a289-5897-47c4-87b5-df1bb7d7c997;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 20082586-8c00-4409-8542-a84f814c1159;
					- m_sourceType = 'F';
					- m_pTarget = GUID d5f08a73-b4dc-458d-b426-efd190717ec2;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_arrow = 2 86 523  86 354  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 176 823 ;
					- m_TargetPort = 1259 823 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIBasicClass 
					- _id = GUID ff2fc4b7-120c-412d-b248-dc900be9cf35;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _subsystem = "Default";
						- _name = "osoba";
						- _id = GUID ede172e5-0022-442c-baa4-d61287322d2d;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "osoba";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.0489381 0 0 0.124343 100.387 119.665 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 176 252  176 1394  1259 1394  1259 252  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID c3ed8ab5-b079-487a-9af9-4d83f33884b4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "osoba";
						- _name = "operator";
						- _id = GUID a3e4d75e-232f-498c-a7e8-07d4be0a776b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ff2fc4b7-120c-412d-b248-dc900be9cf35;
					- m_sourceType = 'F';
					- m_pTarget = GUID d5f08a73-b4dc-458d-b426-efd190717ec2;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_arrow = 2 86 216  86 354  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 176 775 ;
					- m_TargetPort = 1259 823 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID d9e82db3-a2b6-4bdb-9b3f-dbcc485a1971;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "uzytkownik";
						- _name = "osoba";
						- _id = GUID 4ace2de1-fbc7-49dd-9523-5d4b144f1f74;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "osoba";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cb24c3af-a8dd-491d-ae3c-16a2dd8926d2;
					- m_sourceType = 'F';
					- m_pTarget = GUID ff2fc4b7-120c-412d-b248-dc900be9cf35;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_arrow = 2 193 130  193 222  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 176 823 ;
					- m_TargetPort = 1259 823 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID f4cba0f7-7785-4b3d-b62f-981bbb2ac75f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "serwisant";
						- _name = "osoba";
						- _id = GUID c1a7df1d-fdcf-479e-9b63-3db51eaa1b91;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "osoba";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6da1f81c-23ed-404d-aa4c-f35e14063024;
					- m_sourceType = 'F';
					- m_pTarget = GUID ff2fc4b7-120c-412d-b248-dc900be9cf35;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_arrow = 2 193 284  193 222  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 176 759 ;
					- m_TargetPort = 1259 823 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIBasicClass 
					- _id = GUID baa96b8d-7278-45cc-93b5-54d5fd5d162f;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "wybor_akcji";
						- _id = GUID ef67c94a-4027-4480-b2f5-caf0ddb0e76d;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "wybor_akcji";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 360.248 98.0607 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID 47f84bfb-7507-468b-b1dc-2fe18114294a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "uzytkownik";
						- _name = "wybor_akcji";
						- _id = GUID 5349ab45-93ed-4a1e-9fa2-e998cede8f59;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "wybor_pietra";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cb24c3af-a8dd-491d-ae3c-16a2dd8926d2;
					- m_sourceType = 'F';
					- m_pTarget = GUID baa96b8d-7278-45cc-93b5-54d5fd5d162f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1259 815 ;
					- m_TargetPort = -2 444 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 637f9e59-39d3-4c93-8bc1-5ef9739a291f;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "blokada_serwisowa";
						- _id = GUID 4d1276f4-7771-4c7a-a607-0d9c2a4baf5c;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "blokada_serwisowa";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 360.248 428.061 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID ae1d7866-718e-42f8-9e3f-3061931d65d1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "serwisant";
						- _name = "blokada_serwisowa";
						- _id = GUID 89b67664-b2ee-433a-bfc4-a908aaa43c42;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "blokada_serwisowa";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 6da1f81c-23ed-404d-aa4c-f35e14063024;
					- m_sourceType = 'F';
					- m_pTarget = GUID 637f9e59-39d3-4c93-8bc1-5ef9739a291f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1014 1008 ;
					- m_TargetPort = -2 526 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 7f327046-8a73-401d-a026-bffae195cc3b;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "przywolaj_winde";
						- _id = GUID 1d4db3a4-5a19-465e-b39a-eb74a2b88eb1;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "przywolaj_winde";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 784.248 2.06069 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 836e90f3-3652-48f0-9244-7e9a3752a200;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "zamknij_drzwi";
						- _id = GUID 6828abb9-7d10-41fe-a8e1-f882afc19263;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "zamknij_drzwi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 784.248 67.0607 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 7d2adebf-aaab-4723-93e4-c66aebc2de58;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "otworz_drzwi";
						- _id = GUID f96c521b-389e-4a67-bba3-09f94acb07ce;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "otworz_drzwi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 784.248 132.061 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 53d55fba-f684-440e-b9aa-d5191ab72b6a;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "pietro_0";
						- _id = GUID 5a52ca65-93e4-4521-9648-2e80ee27f4eb;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "pietro_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 784.248 197.061 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 84fc0a0f-b721-480e-bf6d-540215a3d50b;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "pietro_1";
						- _id = GUID aba4769d-2c1e-4a9e-94be-33447304f313;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "pietro_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 784.248 262.061 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID dcf9f097-48ee-4fab-a5f8-c8abaaa38afb;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "pietro_2";
						- _id = GUID b2cb7236-a913-4b44-ad87-7f3d68772cde;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "pietro_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 784.248 327.061 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID a657aab1-f411-4a6f-b970-09e57bf88013;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _subsystem = "Default";
						- _class = "blokada_serwisowa";
						- _name = "wybor_akcji";
						- _id = GUID be158430-a382-48b5-bb4c-509c626882bb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 637f9e59-39d3-4c93-8bc1-5ef9739a291f;
					- m_sourceType = 'F';
					- m_pTarget = GUID baa96b8d-7278-45cc-93b5-54d5fd5d162f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 482 -1 ;
					- m_TargetPort = 498 1054 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIBasicClass 
					- _id = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "praca";
						- _id = GUID 1b0f4195-24b6-434a-b917-1d697bbbde58;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "praca";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 562.248 98.0607 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _subsystem = "Default";
						- _name = "start";
						- _id = GUID 12edd612-b6cf-4851-899e-d99a2d2fdd67;
					}
					- m_pParent = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
					- m_name = { CGIText 
						- m_str = "start";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.124004 0 0 0.0606909 500.248 218.061 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIInheritance 
					- _id = GUID 911de1d4-83fd-4768-b028-a64479e56f1c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "praca";
						- _name = "przywolaj_winde";
						- _id = GUID fd30a0af-d20a-4f35-a57e-dc5b52f6fc16;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "przywolaj_winde";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7f327046-8a73-401d-a026-bffae195cc3b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1095 345 ;
					- m_TargetPort = 6 642 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 8c13f868-5c78-4c1a-a8c4-57807e812825;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "praca";
						- _name = "zamknij_drzwi";
						- _id = GUID d5c86939-f2d1-4a9d-9996-186d85d52868;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "zamknij_drzwi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 836e90f3-3652-48f0-9244-7e9a3752a200;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1127 576 ;
					- m_TargetPort = 22 708 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID bf1b44ed-9e8f-4560-8384-eeaeeca0f03a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "praca";
						- _name = "otworz_drzwi";
						- _id = GUID 54a57df8-1686-4f51-a867-05b71e8543c6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "otworz_drzwi";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7d2adebf-aaab-4723-93e4-c66aebc2de58;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1054 790 ;
					- m_TargetPort = 6 460 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 49f77a5b-fd3d-4e12-9664-f81f218309e0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "praca";
						- _name = "pietro_0";
						- _id = GUID 7d75cbf1-f0e4-415e-95db-af6136dde1c3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "pietro_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 53d55fba-f684-440e-b9aa-d5191ab72b6a;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 998 922 ;
					- m_TargetPort = 111 230 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID cf7fd51c-7c46-49ff-b68a-56dfcb09dfbb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "praca";
						- _name = "pietro_1";
						- _id = GUID 9f426fa1-b42d-4a5f-8fc0-c4925334d287;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "pietro_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID 84fc0a0f-b721-480e-bf6d-540215a3d50b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 748 1021 ;
					- m_TargetPort = 103 230 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID a97672f4-af62-4972-98d8-b5bd6a8b1b09;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "praca";
						- _name = "pietro_2";
						- _id = GUID 20fc20c9-5c24-4113-bc58-e3dc5e16a595;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "pietro_2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID dcf9f097-48ee-4fab-a5f8-c8abaaa38afb;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 627 1054 ;
					- m_TargetPort = 111 230 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 99d71c90-606e-45de-83ba-a6d5fb11687a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "start";
						- _name = "wybor_akcji";
						- _id = GUID cd0b220f-2ae1-4d6a-b6cf-3f7dab0622bd;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "wybor_akcji";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_sourceType = 'F';
					- m_pTarget = GUID baa96b8d-7278-45cc-93b5-54d5fd5d162f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 304 65 ;
					- m_TargetPort = 885 955 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID e1b48dcd-3124-4857-a8ba-a716483974d8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "przywolaj_winde";
						- _name = "start";
						- _id = GUID 033cb284-072a-4892-b4e8-ae0cd8bc6d93;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "start";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7f327046-8a73-401d-a026-bffae195cc3b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 240 955 ;
					- m_TargetPort = 1014 213 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 227a4e0e-601b-40b1-b3e0-8698d685019f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "zamknij_drzwi";
						- _name = "start";
						- _id = GUID 4453f444-acd0-4126-8b67-3395aacd6713;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "start";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 836e90f3-3652-48f0-9244-7e9a3752a200;
					- m_sourceType = 'F';
					- m_pTarget = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 111 905 ;
					- m_TargetPort = 1079 312 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 9feb86ef-0d0d-4b37-a064-f1f3a82fb788;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "otworz_drzwi";
						- _name = "start";
						- _id = GUID 0a06eb0b-5903-4232-b27b-ce0f3d241d0f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "start";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7d2adebf-aaab-4723-93e4-c66aebc2de58;
					- m_sourceType = 'F';
					- m_pTarget = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 30 724 ;
					- m_TargetPort = 1127 510 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 6a4df20c-67b7-465a-be61-6dbebb294eb2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "pietro_0";
						- _name = "start";
						- _id = GUID 4668dfaf-99d3-4093-a844-c6b59915fed1;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "start";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 53d55fba-f684-440e-b9aa-d5191ab72b6a;
					- m_sourceType = 'F';
					- m_pTarget = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = -2 609 ;
					- m_TargetPort = 1119 592 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 5e3bb1a3-ed5c-4d6e-b568-0828a273cd34;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "pietro_1";
						- _name = "start";
						- _id = GUID 901cc285-8151-4c39-b78b-baf6eaccd677;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "start";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 84fc0a0f-b721-480e-bf6d-540215a3d50b;
					- m_sourceType = 'F';
					- m_pTarget = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = -2 526 ;
					- m_TargetPort = 1103 691 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4160a7d4-0eff-4382-8fae-9970389ae6ba;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "pietro_2";
						- _name = "start";
						- _id = GUID ca56f1f9-4078-46d9-803c-82f9f9551a9d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "start";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID dcf9f097-48ee-4fab-a5f8-c8abaaa38afb;
					- m_sourceType = 'F';
					- m_pTarget = GUID 10b9f1f1-f1f7-48cb-a538-a9744d131785;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 14 411 ;
					- m_TargetPort = 1014 905 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 17f6f99a-be8c-4769-855b-bac5994adacf;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _subsystem = "Default";
						- _class = "praca";
						- _name = "wybor_akcji";
						- _id = GUID 59b46880-536f-4591-a974-76fbd26ae1b7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "wybor_akcji";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID fc6e56b3-9cac-4a4f-bd0a-4b1ecc0d12b9;
					- m_sourceType = 'F';
					- m_pTarget = GUID baa96b8d-7278-45cc-93b5-54d5fd5d162f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 6 427 ;
					- m_TargetPort = 1127 493 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 577de3e2-e29c-4d68-8819-08c4b975c282;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
				- m_bFreezeCompartmentContent = 0;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _name = "Default";
				- _id = GUID 8bbbc81d-41fc-408b-82d8-7912254c4a0c;
			}
		}
	}
}

